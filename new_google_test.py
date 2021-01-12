from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from random import randint
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

# class input gLFyf gsfi
# id rso


def main():
    while True:
        try:
            driver.find_element_by_name('q').clear()
            key = input('Enter search key:')
            time.sleep(1)
            search = driver.find_element_by_name("q")
            search.send_keys(key)
            search.send_keys(Keys.RETURN)
            try:
                time.sleep = 1
                page_result = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "rso"))
                )
                # yuRUbf
                items = page_result.find_elements_by_class_name(
                    "g")
                elems = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".yuRUbf [href]")))
               # links = [elem.get_attribute('href') for elem in elems]
                if elems:
                    for elem in elems:
                        # elem.click()
                        link = elem.get_attribute('href')
                        tuoitre = 'tuoitre.vn'
                        page_url = 'tuoitre.vn'
                        if page_url in link:
                            elem.click()
                            print('trying to get href from this webpage 0')
                            new_elems = driver.find_elements_by_tag_name(
                                'a')
                            print('trying to get href from this webpage 2')
                            if new_elems:
                                # for new_elem in new_elems:
                                #     print(new_elem.get_attribute("href"))
                                #     if page_url in new_elem.get_attribute("href"):
                                #         print('found')
                                #         new_elem.click()
                                #         break
                                print('trying to extract all the href to array')
                                href = []
                                count = 0
                                for el in new_elems:
                                    if count >= 20:
                                        break
                                    if page_url in el.get_attribute("href"):
                                        print(el.get_attribute("href"))
                                        href.append(el.get_attribute("href"))
                                        count += 1
                                new_url = href[randint(
                                    0, len(href)-1)]
                                print('new url', new_url)
                                driver.get(new_url)
                                print(href)
                                break
                            break
                time.sleep(1)
            except:
                print('ex0')
        except:
            break


if __name__ == '__main__':
    main()
