import re
from os import path, system, name, kill, getpid
from time import sleep
import requests
from lxml.html import document_fromstring

def remove_space_line(x):
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in x.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    y = '\n'.join(chunk for chunk in chunks if chunk)
    return y

def text_replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)

def add_title_fw():
    file_title = title.encode()
    write_to_file.write(file_title)
    title_return = '\n\n'
    file_title_return = title_return.encode()
    write_to_file.write(file_title_return)

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def nomore_page_close(y):
    if 'htm' not in y:
        write_to_file.close()
        print('No more chapter, stop to send request!')
        exit()

replace_symbol_dict = {'-->>': ''}
ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
headers = {'user-agent': ua}
base_url = 'https://www.xinshuhaige.com/135479/3026207.html'
x = 0
# Determine if the file name exists
for n in range(5):
    clear()
    global file_name
    file_name = input('Input a filename:')+'.txt'
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

while True:
    try:
        r = requests.get(base_url, headers=headers, timeout=10)
    except (requests.ConnectionError,
            requests.RequestException,
            requests.HTTPError,
            requests.Timeout,
            requests.TooManyRedirects):
        print('Connection Error! ReConnecting......')
        continue
    r.encoding = r.apparent_encoding
    doc = document_fromstring(r.text)
    title = doc.xpath("/html/body/h1")[0].text_content()
    content = doc.xpath("//div[@class='content']")
    page_content = ''
    for line_content in content:
        page_content += line_content.text_content()+'\n'
    page_content = page_content.replace('喜欢元龙请大家收藏：(m.soxs.cc)元龙搜小说更新速度最快。','')
    write_to_file = open(file_name, 'ab')
    if base_url.find('htm') == -1:
        write_to_file.close()
        print('No more chapters, closing file... done!')
        break
    else:
        np_url = remove_space_line(doc.xpath("(//a[contains(.,'下一章')])[2]")[0].get('href'))
        base_url = 'https://m.soxs.cc'+np_url
        add_title_fw()
        file_context = page_content.encode()
        write_to_file.write(file_context)
        context_return = '\n\n'
        file_context_return = context_return.encode()
        write_to_file.write(file_context_return)
        print(title+' : '+base_url)