import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.button()
        self.initUI()


    def initUI(self):
        label1 = QLabel('', self)
        label1.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap('뮐러.jpg')

        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)  # 이미지 세팅
        self.label.setContentsMargins(0, 0, 0, 0)
        self.label.resize(self.pixmap.width(), self.pixmap.height())



        font1 = label1.font()
        font1.setPointSize(20)



        label1.setFont(font1)

        layout = QVBoxLayout()
        layout.addWidget(label1)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(0, 0, 580, 385)
        self.show()

    def button(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())