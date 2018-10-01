from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')
    # 크롬 브라우저 실행 후 네이버 접속
    rank = driver.find_element_by_class_name('rank_scroll')
    rank_list = rank.find_elements_by_tag_name('li')

    ex = Workbook()
    es = ex.active

    for r in rank_list:
        print(r.text)
    # for r in rank_list:
    #     rank_title = r.find_element_by_tag_name('a')
    #     print(r.text)
    #     print('-' * 20)
    #     es.append([rank_title.text])
    ex.save('20413_자유.xlsx')

except Exception as e:
    print(e)
finally:
    driver.close()

# 만들다 말음.
