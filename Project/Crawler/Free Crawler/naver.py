import requests  # requests 라이브러리를 사용하기 위해 import
from bs4 import BeautifulSoup  # 크롤링에 유용한 BeautifulSoup4 라이브러리 사용
from datetime import datetime  # 시간 정보를 받아오기 위해 datetime 라이브러리 사용
from openpyxl import Workbook  # 엑셀에 실시간 순위를 기록하기 위해 사용하는 라이브러리


def time_check():  # 정보를 수집해온 시간을 출력하기 위해 현재 시간 정보를 반환하는 함수
    now = datetime.now()  # 현재 시간을 now 변수에 저장
    now_time = f"<{now.year}. {now.month}. {now.day} - {now.hour}:{now.minute}\
    기준 네이버 실시간 검색어 순위>"

    return now_time  # 현재 시간 정보를 반환


html = requests.get('https://www.naver.com/').text  # 네이버 html 코드를 html 변수에 저장
soup = BeautifulSoup(html, 'lxml')  # lxml을 이용하여 웹 페이지를 파싱
rank_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
# PM_CL_realtimeKeyword_rolling class에서 class명이 ah_k인 span 형식의 내용만 select로 저장

ex = Workbook()
es = ex.active
# 엑셀에 크롤링 결과를 기록하기 위해 세팅

print(time_check() + "\n")  # 함수에서 반환된 시간 정보 출력 + 개행
for rank, title in enumerate(rank_list, 1):  # enumerate를 이용하여 반복문 실행
    print(rank, title.text)  # 순위와 제목 출력
    temp = f"{rank} {title.text}"  # (순위) (타이틀) 순으로 기록하기 위해 temp에 문자열 저장
    es.append([temp])
    # 엑셀의 각 행에 실시간 순위를 기록

ex.save('20413_자유.xlsx')  # 엑셀 파일 저장
