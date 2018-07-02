from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('https://www.11st.co.kr/')
    # 크롬 브라우저 실행 후 11번가 접속
    search = driver.find_element_by_id('AKCKwd')
    # 검색 창 레이아웃 선택
    search.clear()
    # 검색 창 초기화
    search.send_keys('라즈베리파이')
    # 검색 창에 라즈베리파이 문자열 입력
    search.send_keys(Keys.RETURN)
    # Enter

    elem = driver.find_element_by_class_name('total_listing_wrap')
    # div 태그의 total_listing_wrap 클래스 부분을 따옴
    hotclick_list = elem.find_elements_by_tag_name('li')
    # li 태그를 찾아 리스트를 저장
    ex = Workbook()
    es = ex.active
    # 엑셀 세팅

    for h in hotclick_list:
        title = h.find_element_by_class_name('info_tit')
        # 각 리스트 당 info_tit 클래스 부분을 따옴
        print(title.text)
        # a 태그 사이의 문자열을 출력
        print('-' * 20)
        # 구분선
        es.append([title.text])
        # 엑셀 파일에 title 문자열을 추가
    ex.save('20413_지정.xlsx')
    # 엑셀 파일을 소스코드와 같은 디렉토리에 저장

except Exception as e:
    print(e)

finally:
    driver.close()