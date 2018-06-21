from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('https://www.11st.co.kr/')

    search = driver.find_element_by_id('AKCKwd')
    search.clear()
    search.send_keys('라즈베리파이')
    search.send_keys(Keys.RETURN)

    elem = driver.find_element_by_class_name('info_tit')
    shop_list = elem.find_element_by_tag_name('a')
except Exception as e:
    print(e)

finally:
    driver.close()