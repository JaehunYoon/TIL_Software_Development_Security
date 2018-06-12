from selenium import webdriver
from selenium.webdriver.common.keys import Keys

keyward = input("Please input search query >> ")
driver = webdriver.Chrome('chromedriver')

try:
    driver.get('https://www.naver.com')
    print(driver.title)
    # Ctrl + Shift + C
    elem = driver.find_element_by_id('query')
    elem.clear()  # 검색어에 값이 있을 경우를 대비하여 초기화
    elem.send_keys(keyward)
    elem.send_keys(Keys.RETURN)

    news = driver.find_element_by_class_name('news')
    # news_list = news.find_elements_by_tag_name('li')
    # 위와 같이 코드를 작성하게 되면 li 태그를 가진 하위 뉴스 리스트까지 불러오게 됨.
    # 오류 발생
    news_list = news.find_elements_by_xpath('./ul/li')

    for n in news_list:
        news_title = n.find_element_by_class_name('_sp_each_title')
        print(news_title.text)
        print('-' * 20)
    # for post in news_list:
    #     post_title = post.find_element_by_tag_name('dt')
    #     main_title = post_title.find_element_by_tag_name('a')
    #     print(main_title.get_attribute('title'))
    #     print(main_title.get_attribute('href'))
    #     print('-' * 20)

except Exception as e:
    print(e)
finally:
    driver.quit()