import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)  # UI 파일 로드

        # 버튼 클릭 시 Calender 날짜를 date_move로 설정
        self.button_calende_move.clicked.connect(self.update_calendar)

    def update_calendar(self):
        date = self.date_move.date()  # QDate 객체
        self.Calender.setSelectedDate(date)  # Calender에 설정

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
