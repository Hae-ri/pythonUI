import sys

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('ui/calculator_app.ui')[0] # ui 불러오기

class CalculatorApp(QMainWindow, form_class):
    def __init__(self): # 초기화자(자바의 생성자와 비슷)
        super().__init__()
        self.setupUi(self) # 초기값, 만들어 놓은 test.ui 연결
        self.setWindowTitle('초간단 계산기') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/calculator_icon.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Calculator Application Ver 1.0')
        
        self.clear_button.clicked.connect(self.clear_text)

        self.num1_button.clicked.connect(self.num1_button_clicked)
        self.num2_button.clicked.connect(self.num2_button_clicked)
        self.num3_button.clicked.connect(self.num3_button_clicked)
        self.num4_button.clicked.connect(self.num4_button_clicked)
        self.num5_button.clicked.connect(self.num5_button_clicked)
        self.num6_button.clicked.connect(self.num6_button_clicked)
        self.num7_button.clicked.connect(self.num7_button_clicked)
        self.num8_button.clicked.connect(self.num8_button_clicked)
        self.num9_button.clicked.connect(self.num9_button_clicked)
        self.num0_button.clicked.connect(self.num0_button_clicked)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.sub_button.clicked.connect(self.sub_button_clicked)
        self.mul_button.clicked.connect(self.mul_button_clicked)
        self.div_button.clicked.connect(self.div_button_clicked)
        self.dot_button.clicked.connect(self.dot_button_clicked)

        self.result_button.clicked.connect(self.result_button_clicked)


    def num1_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal + '1')


    def num2_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '2')

    def num3_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '3')

    def num4_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '4')

    def num5_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '5')

    def num6_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '6')

    def num7_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '7')

    def num8_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '8')

    def num9_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '9')

    def num0_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '0')

    def dot_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal + '.')

    def add_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal + '+')

    def sub_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '-')

    def mul_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '*')

    def div_button_clicked(self):
        cal = self.result_label.text()
        self.result_label.setText(cal+ '/')



    def result_button_clicked(self):
        cal = self.result_label.text()
        result = eval(cal) # 문자열 계산식을 계산해 줌 ('=' 클릭하면)
        self.result_label.setText(f'{cal}={result}')




    def clear_text(self):
        self.result_label.clear()



app = QApplication(sys.argv)
window = CalculatorApp()
window.show()
app.exec_()





# cal = ''
#
# num1 = input('첫번째 클릭한 숫자: ')
# cal = cal + num1
# # print(cal)
# op1 = input('첫번째 클릭한 연산자: ')
# cal = cal + op1
# # print(cal)
# num2 = input('두번째 클릭한 숫자: ')
# cal = cal + num2
# # print(cal)
#
# result = eval(cal) # 문자열 계산식을 계산해 줌 ('=' 클릭하면)
# print(f'{cal}={result}')
#
# # 'c' 클릭하면 내용 지우고, cal='' 으로 초기화