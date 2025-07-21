from PyQt5.QtWidgets import QCalendarWidget, QDateEdit, QPushButton
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateTimeEdit

class SliderWindowOpacityController:
    """슬라이더로 메인 윈도우 전체의 투명도 조절"""
    def __init__(self, slider, label, window):
        self.slider = slider
        self.window = window
        self.label = label

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.init_connection()
        self.update_opacity(self.slider.value())  # 초기 투명도 반영
        self.update_label(self.slider.value())  #초기화 100

    def init_connection(self):
        self.slider.valueChanged.connect(self.update_opacity) # slider값에 따라 투명화
        self.slider.valueChanged.connect(self.update_label)  #label, slider 동기화

    def update_opacity(self, value):
        opacity = value / 100
        self.window.setWindowOpacity(opacity)
    
    def update_label(self, value):
        self.label.setText(str(value))


class CalendarController:
    '''DateEdit 설정'''
    def __init__(self, calendar_widget: QCalendarWidget):
        self.calendar = calendar_widget

    def set_date(self, date: QDate):
        self.calendar.setSelectedDate(date)

    def get_date(self) -> QDate:
        return self.calendar.selectedDate()


class CalendarDateSyncController:
    """calendar ↔ date_edit 간 양방향 동기화"""
    def __init__(self, calendar: QCalendarWidget, date_edit: QDateEdit):
        self.calendar = calendar
        self.date_edit = date_edit
        self.connect_signals()

    def connect_signals(self):
        # calendar → date_edit
        self.calendar.selectionChanged.connect(self.sync_to_date_edit)

        # date_edit → calendar
        self.date_edit.dateChanged.connect(self.sync_to_calendar)

    def sync_to_date_edit(self):
        date = self.calendar.selectedDate()
        self.date_edit.setDate(date)

    def sync_to_calendar(self, date: QDate):
        self.calendar.setSelectedDate(date)


class DateEditController:
    def __init__(self, date_edit: QDateEdit):
        self.date_edit = date_edit
        self.init_format()

    def init_format(self):
        self.date_edit.setDisplayFormat("yyyy-MM-dd")  # 표시 형식 고정
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCurrentSection(QDateTimeEdit.DaySection)  # ▲ 누르면 "일"이 올라감

    def get_date(self) -> QDate:
        return self.date_edit.date()

    def set_date(self, date: QDate):
        self.date_edit.setDate(date)

    def set_today(self):
        self.set_date(QDate.currentDate())


class ButtonController:
    def __init__(self, button_widget: QPushButton):
        self.button = button_widget

    def on_click(self, callback):
        self.button.clicked.connect(callback)

    def on_click_sync_calendar(self, date_edit: QDateEdit, calendar: QCalendarWidget):
        """버튼 클릭 시 date_edit의 날짜를 calendar에 반영"""
        def sync():
            date = date_edit.date()
            calendar.setSelectedDate(date)
        self.button.clicked.connect(sync)
