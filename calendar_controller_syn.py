from PyQt5.QtWidgets import QDateTimeEdit
from PyQt5.QtWidgets import QCalendarWidget, QDateEdit
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QTimer


class CalendarController:
    '''DateEdit 설정'''
    def __init__(self, calendar_widget: QCalendarWidget):
        self.calendar = calendar_widget

    def set_date(self, date: QDate):
        self.calendar.setSelectedDate(date)

    def get_date(self) -> QDate:
        return self.calendar.selectedDate()
    

class DateEditController:
    def __init__(self, date_edit: QDateEdit):
        self.date_edit = date_edit
        self.init_format()

    def init_format(self):
        self.date_edit.setDisplayFormat("yyyy-MM-dd")  # 표시 형식 고정
        self.date_edit.setDate(QDate.currentDate())
        #self.date_edit.setCurrentSection(QDateTimeEdit.DaySection)  # ▲ 누르면 "일"이 올라감
        QTimer.singleShot(0, lambda: self.date_edit.setCurrentSection(QDateTimeEdit.DaySection))

    def get_date(self) -> QDate:
        return self.date_edit.date()

    def set_date(self, date: QDate):
        self.date_edit.setDate(date)

    def set_today(self):
        self.set_date(QDate.currentDate())


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
