import sys
import threading

from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

import requests
from bs4 import BeautifulSoup

form_class = uic.loadUiType('ui/weatherApp.ui')[0] # ui 불러오기

class WeatherCrawler(QThread): # 스레드 클래스로 선언
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def weather_crawling(self, weather_area):
        weather_result = [] # 날씨 크롤링 결과를 반환할 빈 리스트 생성

        weather_html = requests.get(f'https://search.naver.com/search.naver?query={weather_area}날씨')

        weather_soup = BeautifulSoup(weather_html.text, 'html.parser')  # 파싱한 응답결과 html

        try:
            area_title = weather_soup.find('h2', {'class': 'title'}).text  # 날씨를 검색한 지역명 크롤링

            today_temperature = weather_soup.find('div', {'class': 'temperature_text'}).text  # 오늘 기온 크롤링
            today_temperature = today_temperature[6:9].strip()  # 오늘 기온만 인덱싱한 후 양쪽 공백문자 제거

            yesterday_weather = weather_soup.find('p', {'class': 'summary'}).text  # 어제 날씨 비교 크롤링
            yesterday_weather = yesterday_weather[0:13].strip()  # 어제 날씨 비교 인덱싱한 후 양쪽 공백문자 제거

            today_weather = weather_soup.find('span', {'class': 'weather before_slash'}).text  # 오늘 날씨(맑음, 흐림, 구름 많음 등)

            today_rain = weather_soup.find('dd', {'class': 'desc'}).text  # 강수 확률

            dust_info = weather_soup.find_all('span', {'class': 'txt'})  # 미세먼지 정보
            dust1 = dust_info[0].text  # 미세먼지
            dust2 = dust_info[1].text  # 초미세먼지

        except:  # 예외처리(국내 지역 외 검색 시)
            try:
                # 해외 도시 검색 시 크롤링될 태그 정의
                area_title = weather_soup.find('span', {'class': 'btn_select'}).text  # 날씨를 검색한 해외 지역명 크롤링
                area_title = area_title.strip()
                today_temperature = weather_soup.find('span', {'class': 'todaytemp'}).text  # 오늘 기온 크롤링
                today_temperature = f'{today_temperature}°'
                today_weather = weather_soup.find('p', {'class': 'cast_txt'}).text  # 오늘 날씨(맑음, 흐림, 구름 많음 등)
                today_weather = today_weather[0:2].strip()
                yesterday_weather = weather_soup.find('p', {'class': 'cast_txt'}).text
                today_rain = '-'
                dust1 = '-'
                dust2 = '-'

            except:
                area_title = '검색한 지역은 날씨 정보가 없음'
                today_weather = '-'
                today_temperature = '-'
                yesterday_weather = '-'
                today_rain = '-'
                dust1 = '-'
                dust2 = '-'

        weather_result.append(area_title)
        weather_result.append(today_temperature)
        weather_result.append(today_weather)
        weather_result.append(yesterday_weather)
        weather_result.append(today_rain)
        weather_result.append(dust1)
        weather_result.append(dust2)

        return weather_result

class WeatherApp(QMainWindow, form_class):
    def __init__(self,parent=None): # 초기화자(자바의 생성자와 비슷)
        super().__init__(parent)
        self.setupUi(self) # 초기값, 만들어 놓은 test.ui 연결
        self.setWindowTitle('오늘의 날씨') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/weather_icon.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Weather Application Ver 1.0')
        self.weatherInfo = WeatherCrawler(self) # 날씨크롤러클래스의 객체를 생성

        self.search_Button.clicked.connect(self.weather_search)
        self.search_Button.clicked.connect(self.reflash_function)

    def closeEvent(self):
        self.weatherInfo.close()

    def reflash_function(self):
        # self.weather_search()
        threading.Timer(600,self.weather_search).start()

    def weather_search(self):
        input_area = self.area_input.text() # area_input에 입력된 지역명 가져오기
        if input_area =='':
            QMessageBox.about(self,'입력오류','지역명을 입력하세요.')

            # 스레드 클래스의 weather_crawling 메소드 호출
            # weather_crawling 함수의 리턴값 저장(크롤링한 날씨 정보 리스트)
        else:
            weather_data = self.weatherInfo.weather_crawling(input_area)

            self.area_label.setText(weather_data[0])
            if weather_data[2] == '맑음':
                weather_image = QPixmap('img/sun.png')
                self.weather_label.setPixmap(QPixmap(weather_image))
            elif weather_data[2] == '흐림':
                weather_image = QPixmap('img/cloud.png')
                self.weather_label.setPixmap(QPixmap(weather_image))
            elif weather_data[2] == '구름많음':
                weather_image = QPixmap('img/cloud.png')
                self.weather_label.setPixmap(QPixmap(weather_image))
            elif weather_data[2] == '눈':
                weather_image = QPixmap('img/snow.png')
                self.weather_label.setPixmap(QPixmap(weather_image))
            elif weather_data[2] == '비':
                weather_image = QPixmap('img/rain.png')
                self.weather_label.setPixmap(QPixmap(weather_image))
            else:
                self.weather_label.setText(weather_data[2])
            self.temper_label.setText(weather_data[1])
            self.yesterday_label.setText(weather_data[3])
            self.rain_label.setText(weather_data[4])
            self.dust1_label.setText(weather_data[5])
            self.dust2_label.setText(weather_data[6])



app = QApplication(sys.argv)
window = WeatherApp()
window.show()
app.exec_()