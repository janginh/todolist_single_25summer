# smart_date_edit.py
from PyQt5.QtWidgets import QDateEdit, QDateTimeEdit
from PyQt5.QtCore import QDate, Qt

class SmartDateEdit(QDateEdit):
    def stepBy(self, steps: int):
        current = self.date()
        section = self.currentSection()

        if section == QDateTimeEdit.DaySection:
            new_date = current.addDays(steps)
        elif section == QDateTimeEdit.MonthSection:
            new_date = current.addMonths(steps)
        elif section == QDateTimeEdit.YearSection:
            new_date = current.addYears(steps)
        else:
            new_date = current  # fallback

        self.setDate(new_date)

    def showEvent(self, event):
        super().showEvent(event)
        self.setCalendarPopup(True)  # UI에서 누락됐을 경우를 대비
        # 섹션 자동 설정 제거 (사용자가 클릭한 곳 기준으로 동작해야 함)

    def focusInEvent(self, event):
        super().focusInEvent(event)
        # 섹션 고정 제거 → 사용자가 클릭한 위치에 따라 동작하게
