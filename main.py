import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate, QTimer
from PyQt5.QtWidgets import QDateTimeEdit, QDateEdit
from slider_opacity import SliderWindowOpacityController
from calendar_controller_syn import (
    CalendarController,
    DateEditController,
    CalendarDateSyncController
)
from button_controller import ButtonController
from smart_date_edit import SmartDateEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)

# 기존 QDateEdit → SmartDateEdit으로 대체
        geom = self.date_move.geometry()
        self.smart_date_edit = SmartDateEdit(self)
        self.smart_date_edit.setGeometry(geom)
        self.smart_date_edit.setObjectName("date_move")
        self.smart_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.smart_date_edit.setDate(QDate.currentDate())
        self.smart_date_edit.show()
        self.date_move.hide()
        
    # 캘린더 관련 내용
        # Calender 초기화
        self.calendar_controller = CalendarController(self.Calender) #캘린더
        
        #캘린더 위 date controller 초기화
        self.date_edit_controller = DateEditController(self.smart_date_edit) 
        self.date_edit_controller.set_today() #오늘날짜로 초기화
        
        #date controller button 초기화
        self.button_controller = ButtonController(self.button_calende_move) #캘린더 날짜 버튼
        #버튼을 통해 datecontroller - Calender 연결
        self.button_controller.on_click_sync_calendar(self.smart_date_edit, self.Calender)
        
        # #calender, dateEdit 서로 동기화
        self.calendar_date_sync = CalendarDateSyncController(self.Calender, self.smart_date_edit)


    #투명화 관련 내용
        # slider, label 동기화, label값에 따라 투명화
        self.window_opacity_controller = SliderWindowOpacityController(self.slider_opacity, self.label_opacity, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
