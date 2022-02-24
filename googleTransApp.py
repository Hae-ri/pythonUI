import sys

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import googletrans

form_class = uic.loadUiType('ui/googletrans_ui.ui')[0] # ui 불러오기

class TransApp(QMainWindow, form_class):
    def __init__(self): # 초기화자(자바의 생성자와 비슷)
        super().__init__()
        self.setupUi(self) # 초기값, 만들어 놓은 test.ui 연결
        self.setWindowTitle('한줄 번역기') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/googlelogo.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Google Trans Application Ver 1.0')

        self.trans_Button.clicked.connect(self.trans_Button_clicked)
        self.clear_Button.clicked.connect(self.clear_text)  # 클리어 버튼 클릭 시 연결될 함수 설정

    def trans_Button_clicked(self):
        trans_txt = self.kor_input.text()
        trans = googletrans.Translator()

        eng = trans.translate(trans_txt, dest='en') # 영어 번역 결과
        ja = trans.translate(trans_txt, dest='ja') # 일본어 번역 결과
        zh_cn = trans.translate(trans_txt, dest='zh-cn') # 중국어 번역 결과

        self.eng_result.setText(eng.text)
        self.ja_result.setText(ja.text)
        self.zh_cn_result.setText(zh_cn.text)


    def clear_text(self):
        self.kor_input.clear()
        self.eng_result.clear()
        self.ja_result.clear()
        self.zh_cn_result.clear()


app = QApplication(sys.argv)
window = TransApp()
window.show()
app.exec_()