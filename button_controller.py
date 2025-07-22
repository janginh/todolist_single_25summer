from PyQt5.QtWidgets import QCalendarWidget, QDateEdit, QPushButton

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
