import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from widgets import (
    CalendarController, 
    DateEditController, 
    ButtonController, 
    SliderWindowOpacityController,
    CalendarDateSyncController
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)

        # Calender 초기화
        self.calendar_controller = CalendarController(self.Calender) #캘린더
        
        #캘린더 위 date controller 초기화
        self.date_edit_controller = DateEditController(self.date_move) 
        self.date_edit_controller.set_today() #오늘날짜로 초기화
        
        #date controller button 초기화
        self.button_controller = ButtonController(self.button_calende_move) #캘린더 날짜 버튼
        #버튼을 통해 datecontroller - Calender 연결
        self.button_controller.on_click_sync_calendar(self.date_move, self.Calender) 
        
        # slider, label 동기화, label값에 따라 투명화
        self.window_opacity_controller = SliderWindowOpacityController(self.slider_opacity, self.label_opacity, self)
        #calender, dateEdit 서로 동기화
        self.calendar_date_sync = CalendarDateSyncController(self.Calender, self.date_move)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
