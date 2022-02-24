import googletrans

trans = googletrans.Translator() # 구글 번역 클래스 Translator로 객체 생성

ret1 = trans.translate('나는 한국인입니다.', dest='en')
ret2 = trans.translate('I like burger.', dest='ko')

eng = trans.translate('나는 한국인입니다.', dest='en')


print(ret1.text)
print(ret2.text)
print(eng.text)

# print(googletrans.LANGUAGES)