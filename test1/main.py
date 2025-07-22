import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from widgets import (
    CalendarController, 
    DateEditController, 
    ButtonController, 
    SliderWindowOpacityController,
    CalendarDateSyncController,
    SmartDateEdit
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)

        # 기존 date_move의 geometry와 부모를 가져와서 SmartDateEdit 생성
        geom = self.date_move.geometry()
        self.smart_date_edit = SmartDateEdit(self)
        self.smart_date_edit.setGeometry(geom)
        self.smart_date_edit.setObjectName("date_move")
        self.smart_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.smart_date_edit.show()
        self.date_move.hide()  # 기존 QDateEdit 숨김

        # 컨트롤러에 SmartDateEdit 연결
        self.calendar_controller = CalendarController(self.Calender)
        self.date_edit_controller = DateEditController(self.smart_date_edit)
        self.date_edit_controller.set_today()

        self.button_controller = ButtonController(self.button_calende_move)
        self.button_controller.on_click_sync_calendar(self.smart_date_edit, self.Calender)

        self.window_opacity_controller = SliderWindowOpacityController(
            self.slider_opacity, self.label_opacity, self
        )

        self.calendar_date_sync = CalendarDateSyncController(
            self.Calender, self.smart_date_edit
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
