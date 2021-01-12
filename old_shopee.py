from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
PATH = 'C:\Program Files (x86)\chromedriver.exe'

# proxy = "115.79.141.127:53281"
# proxy = "115.79.141.127:53281"
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#    "httpProxy":proxy,
#    "ftpProxy":proxy,
#    "sslProxy":proxy,
#    "noProxy":None,
#    "proxyType":"MANUAL",
#    "class":"org.openqa.selenium.Proxy",
#    "autodetect":False
# }
PROXY = "51.81.82.175:80"  # IP:PORT or HOST:PORT

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)

# driver = webdriver.Chrome(PATH, options=chrome_options)
driver = webdriver.Chrome(PATH)
driver.get('https://google.com.vn')
main_page = driver.current_window_handle


def switch_window():
    # __CONFIRM__
    login_page = main_page
    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle
            print('trying to switch login page')
    driver.switch_to.window(login_page)
    try:
        email = driver.find_element_by_id('email')
        password = driver.find_element_by_id('pass')
        if email and password:
            print('input field capture')
            email.send_keys('tuanvip0100')
            password.send_keys('lckviktor')
            login = driver.find_element_by_name('login')
            if login:
                print('login btn detected, trying to login')
                login.click()
                time.sleep(2)
                try:
                    confirm = driver.find_element_by_name('__CONFIRM__')
                    if confirm:
                        print('confirm btn detected')
                        confirm.click()
                        time.sleep(2)
                except:
                    print('wrong username or password')
                driver.switch_to_window(main_page)
                scroll('down')
                access_comment_rating()
    except:
        print('can not capture input')


def scroll(option):
    if option == 'down':
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(500, 1000)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(1000, 1500)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(1500, 2000)")
        time.sleep(2)
    if option == 'up':
        driver.execute_script("window.scrollTo(500, 0)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(1000, 500)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(1500, 1000)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(2000, 1500)")
        time.sleep(2)


def scroll_option(option):
    a = 0
    b = 500
    if option == 'down':
        script = "window.scrollTo(" + a + "," + " " + b + ")"


def login_by_facebook():
    try:
        fb_login_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "_1p6-r9"))
        )
        if fb_login_btn:
            print('detect login page')
            items = fb_login_btn.find_elements_by_class_name(
                "WEKQ8O")
            if items:
                print('fb_login detected')
                time.sleep(2)
                for i in items:
                    i.click()
                    switch_window()
                    break
    except:
        print('not found fb btn')


def access_like_button():
    try:
        print("trying to access like btn")
        comment_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "shopee-product-comment-list"))
        )
        if comment_list:
            print('btn list detected')
            items = comment_list.find_elements_by_class_name(
                "shopee-product-rating__like-button")
            if items:
                print('btn detect')
                count = 1
                for i in items:
                    print(count)
                    print('btn')
                    if count == 1:
                        time.sleep(2)
                        i.click()
                        login_by_facebook()
                        driver.switch_to.window(main_page)
                        break
                    count += 1
    except:
        print('no like btn list')


def access_comment_rating():
    try:
        # a = 0
        # b = 500
        # script = "window.scrollTo(" + a + "," + " " + b + ")"
        # driver.execute_script(script)
        print("trying to access comment rating")
        comment_rating = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "product-rating-overview"))
        )
        rating_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "product-ratings__header"))
        )
        if rating_header:
            print('found rating header')
            driver.execute_script(
                "arguments[0].scrollIntoView();", rating_header)
        if comment_rating:
            print('comment detected')
            items = comment_rating.find_elements_by_class_name(
                "product-rating-overview__filter")
            if items:
                count = 1
                for i in items:
                    if count == 2:
                        print(i.text)
                        time.sleep(2)
                        i.click()
                        time.sleep(2)
                        access_like_button()
                        break
                    count += 1
    except:
        print('no comment rating')


def main():
    while True:
        try:
            driver.find_element_by_class_name(
                "shopee-popup__close-btn").click()
            time.sleep(1)
        except:
            key = input('Enter search key:')
            time.sleep(1)
            search = driver.find_element_by_class_name(
                "shopee-searchbar-input__input")
            search.send_keys(key)
            search.send_keys(Keys.RETURN)
            try:
                main = WebDriverWait(driver, 500).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "shopee-search-item-result__items"))
                )
                items = main.find_elements_by_class_name(
                    "shopee-search-item-result__item")
                if items:
                    print('has items')
                rd = random.randint(1, 10)
                scroll('down')
                try:
                    btn = WebDriverWait(driver, 500).until(
                        EC.presence_of_element_located(
                            (By.CLASS_NAME, "shopee-page-controller"))
                    )
                    if btn:
                        print('page detected')
                except:
                    print('no page')
                item_postion = random.randrange(1, 10)
                count = 1
                const_title = "Điện thoại iPhone 8 Plus Quốc tế 64GB Mới 99% Bảo Hành 12 Tháng"
                print('items found:', len(items))
                if items:
                    for item in items:
                        title = item.find_element_by_class_name("_1NoI8_")
                        if title:
                            print(title.text)
                        if title.text == const_title:
                            # _1NoI8_ _16BAGk
                            item.click()
                            if rd == 1:
                                time.sleep(3)
                                driver.back()
                                # time.sleep(2)
                                # search.send_keys(Keys.RETURN)
                                break
                            else:
                                scroll('down')
                                access_comment_rating()
                                break
                        count += 1
                time.sleep(2)
            except:
                print("ex")


if __name__ == '__main__':
    main()
