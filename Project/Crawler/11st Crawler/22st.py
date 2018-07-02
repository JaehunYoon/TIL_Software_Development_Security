from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('http://www.11st.co.kr/html/main.html')

    elem = driver.find_element_by_id('AKCKwd')
    elem.clear()
    elem.send_keys('라즈베리파이')
    elem.send_keys(Keys.RETURN)
    
    hotclick = driver.find_element_by_class_name('total_listing_wrap')
    hotclick_list = hotclick.find_elements_by_tag_name('li')
    ex = Workbook()
    es = ex.active

    for item in hotclick_list:
        item_list = item.find_element_by_class_name('info_tit')
        print(item_list.text)
        es.append([item_list.text])
    ex.save('20413_십일번가.xlsx')

except Exception as e:
    print(e)

finally:
    driver.close()