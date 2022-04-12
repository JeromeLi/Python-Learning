# import re
# from termcolor import colored
# import backoff
from os import path, system, name, kill, getpid
from time import sleep
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
# from bs4 import BeautifulSoup
from lxml.cssselect import etree, CSSSelector
import requests
# from requests.exceptions import HTTPError
# from lxml.html import document_fromstring


# def remove_space_line(x):
#     # break into lines and remove leading and trailing space on each
#     lines = (line.strip() for line in x.splitlines())
#     # break multi-headlines into a line each
#     chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#     # drop blank lines
#     y = '\n'.join(chunk for chunk in chunks if chunk)
#     return y


# def text_replace(string, substitutions):
#     substrings = sorted(substitutions, key=len, reverse=True)
#     regex = re.compile('|'.join(map(re.escape, substrings)))
#     return regex.sub(lambda match: substitutions[match.group(0)], string)


# def add_title_fw(title):
#     file_title = title.encode()
#     savetofile.write(file_title)
#     title_return = '\n\n'
#     file_title_return = title_return.encode()
#     savetofile.write(file_title_return)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def nomore_page_close(y):
    if 'htm' not in y:
        savetofile.close()
        print('No more chapter, stop to send request!')

# Determine if the file name exists and set file_name
def get_file_name():
    file_name = ''
    for n in range(5):
        clear()
        file_name = input('Input a filename:')
        if not path.exists(file_name):
            break
        else:
            if n == 4:
                print('Are you kidding me?')
                print('Program is terminating.....')
                sleep(2)
                kill(getpid(), 9)
            print('The file name is existed! Please input another file name.')
            sleep(2)
    return file_name

class SaveText:

    def __init__(self, filename, content):
        self.content = content
        self.filename = filename
    def title(self):
        title_byte = bytes(self.content, 'utf-8')
        with open(self.filename, 'ab') as savetofile:
            savetofile.write(title_byte)
            add_return = '\n\n'
            add_return_byte = bytes(add_return, 'utf-8')
            savetofile.write(add_return_byte)
    def article(self):
        article_byte = bytes(self.content,'utf-8')
        with open(self.filename, 'ab') as savetofile:
            savetofile.write(article_byte)
            add_return = '\n\n\n'
            add_return_byte = bytes(add_return, 'utf-8')
            savetofile.write(add_return_byte)

# replace_symbol_dict = {'-->>': ''}

    '''
    base_url = ''
    ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {'user-agent': ua}
    x = 0
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    brower = webdriver.Firefox(firefox_options=fireFoxOptions)
    brower.get('https://www.yeziwx.com/xiaoshuo/xiuluoshenzu/4859876.html')
    print(brower.page_source)
    # instantiate a chrome options object so you can set the size and headless preference

    prefs = {
    'profile.default_content_setting_values': {
    'images': 2,    # 禁用图片的加载
    # 'javascript': 2 ##禁用js，可能会导致通过js加载的互动数抓取失效
    }
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless") # 不弹出浏览器
    browser.implicitly_wait(5) # 操作、获取元素时的隐式等待时间
    browser.set_page_load_timeout(15) # 页面加载超时等待时间
    chrome_options.add_argument("--window-size=1920x1080")
    lucky_button = driver.find_element_by_css_selector("[name=btnI]")
    lucky_button.click()
    '''

# base_url = input('Input a url:')
# base_url = 'https://m.soxs.cc/DaZhuZai/647151.html'
base_url = 'https://m.soxs.cc/DaZhuZai/648757.html'
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")
browser = webdriver.Chrome(options=chrome_options)
browser.set_page_load_timeout(30)
driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/local/bin/chromedriver')
driver.get(base_url)


filename = get_file_name()

while True:

    try:
        print(driver.current_url, driver.title)
        html_title_str = driver.find_element_by_xpath("/html/body/h1").text
        html_str = driver.find_element_by_xpath("//div[@class='content']").text
        html_str = html_str.replace('喜欢大主宰请大家收藏：(m.soxs.cc)大主宰搜小说更新速度最快。','')
        save = SaveText(filename, html_title_str)
        save.title()
        save = SaveText(filename, html_str)
        save.article()
        print ("continue...")
        driver.find_element_by_xpath("//body[@id='chapter']/div[7]/a[3][contains(text(),'下一章')]").click()

    except NoSuchElementException:
        print('No more chapters, closing file... done!')
        driver.close()
        driver.quit()
        break
quit()