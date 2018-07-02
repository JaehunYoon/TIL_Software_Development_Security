'''
[원하는 내용 자유롭게 크롤링하는 크롤러(8점)]

* 크롤링하고자 하는 요소 : 네이버 실시간 검색어 순위

* 크롤링하고자 하는 목적 : 실시간 검색어 순위 결과를 문서로 기록하는 것을 자동화

* 크롤러 동작과정
- requests 라이브러리를 이용하여 네이버 메인페이지 html 소스코드를 html 변수에 저장
- BeautifulSoup4 라이브러리를 이용하여 lxml로 웹 페이지를 파싱
- html 코드 내에서 PM_CLrealtimeKeyword_rolling 이라는 class 중 class명이 ah_k인 span 태그의 내용만 선택하여 rank_list 변수에 저장
- 크롤링 당시의 시각과 크롤링 결과를 cmd 창에 출력
- for 문이 반복될 때마다 엑셀에 한 행씩 순위와 타이틀을 기록
- 반복문이 종료되면 엑셀 파일을 저장
- 프로그램 종료

* 크롤러 기대 효과
: 현재는 프로그램 실행 당시의 실시간 검색어 순위만을 기록하고 프로그램이 종료되지만,
: 추후에 이를 반복문으로 처리하여 DB에 주기적으로 크롤링 결과를 저장한 후,
: 엑셀에 연계하여 보다 정밀하고 신뢰도 있으며 유용한 통계자료를 만들 수 있을 것이다.
'''

import requests  # requests 라이브러리를 사용하기 위해 import
from os import system  # clear screen 기능을 사용하기 위해 os 라이브러리에서 system 함수를 import
from bs4 import BeautifulSoup  # 크롤링에 유용한 BeautifulSoup4 라이브러리 사용
from time import sleep  # 시간 간격을 주어 실시간 검색어 순위를 주기적으로 업데이트하기 위해 time 라이브러리에서 sleep 함수를 import
from datetime import datetime  # 시간 정보를 받아오기 위해 datetime 라이브러리 사용
from openpyxl import Workbook # 엑셀에 실시간 순위를 기록하기 위해 사용하는 라이브러리

def time_check():  # 정보를 수집해온 시간을 출력하기 위해 현재 시간 정보를 반환하는 함수
    now = datetime.now()  # 현재 시간을 now 변수에 저장
    now_time = f"<{now.year}. {now.month}. {now.day} - {now.hour}:{now.minute} 기준 네이버 실시간 검색어 순위>"

    return now_time  # 현재 시간 정보를 반환


html = requests.get('https://www.naver.com/').text  # 네이버 html 소스코드를 html 변수에 저장
soup = BeautifulSoup(html, 'lxml')  # lxml을 이용하여 웹 페이지를 파싱
rank_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
# PM_CL_realtimeKeyword_rolling 라는 class에서 class명이 ah_k인 span 태그 형식의 내용만 select로 저장

ex = Workbook()
es = ex.active
# 엑셀에 크롤링 결과를 기록하기 위해 세팅

print(time_check() + "\n")  # 함수에서 반환된 시간 정보 출력 + 개행
for rank, title in enumerate(rank_list, 1):  # Python 내장함수인 enumerate를 이용하여 반복문 실행
    print(rank, title.text)  # 순위와 제목 출력
    temp = "{} {}".format(rank, title.text)  # (순위) (타이틀) 순으로 기록하기 위해 temp에 문자열 저장
    es.append([temp])  # 엑셀의 각 행에 실시간 순위를 기록

ex.save('20413_자유.xlsx')  # 엑셀 파일 저장
