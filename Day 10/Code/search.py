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

    blogs = driver.find_element_by_class_name('_blogBase')
    blogs_list = blogs.find_elements_by_tag_name('li')
    # type(blogs_list) = list()
    for post in blogs_list:
        # print(post.text)
        # print('-' * 20)

        post_title = post.find_element_by_class_name('sh_blog_title')
        # print(post_title.text)
        print(post_title.get_attribute('title'))
        print(post_title.get_attribute('href'))
        print('-' * 20)
        # 여기서 한 가지 의문이 들 수가 있다.
        # 그 의문을 찾아내 볼 것
        # => ...으로 title이 생략되어 있는 부분의 제목을 출력하기 => 속성 : title
        # 응용 : 링크되는 사이트의 URL을 같이 출력해볼 것

except Exception as e:
    print(e)
finally:
    driver.quit()