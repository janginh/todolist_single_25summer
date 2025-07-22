from PyQt5.QtWidgets import QSlider, QLabel, QWidget

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
