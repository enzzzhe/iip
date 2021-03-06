import hashlib
import urllib.request
import bs4
import os
import re


def url_search(url):
    url_file_path = "url.txt"

    if not os.path.exists(url_file_path):
        print('url.txt doesn\'t exist: creating new one')
        url_file = open('url.txt', 'w')
    else:
        print('url.txt has been found')
        url_file = open('url.txt', 'r+')

    if not (os.stat(url_file_path)).st_size:
        print('url.txt is empty: creating new line with current url input')
        url_file.write(url + '\n')
        return

    for line in url_file:
        if line == url:
            print('current url input has been found in url.txt')
            return

    url_file.write(url + '\n')
    print('current url input hasn\'t been found in url.txt: creating new line with current url input')
    return


def file_search_flag(path):
    if os.path.exists(path):
        print('content.bin has been found')
        return True
    else:
        print('content.bin hasn\'t been found in directory: creating new one')
        return False


def wiki_parser(url: str, base_path: str):
    url_search(url)

    random_hex = (hashlib.md5(url.encode())).hexdigest()
    directory_path = f"{base_path}/{random_hex}"

    if not os.path.exists(directory_path):
        print('such base_path doesn\'t exist: creating new one')
        os.makedirs(directory_path)

    directory_path = directory_path + '\\content.bin'

    content_file_exists = file_search_flag(directory_path)

    if not content_file_exists:
        with open(directory_path, 'wb') as content:
            page_content = urllib.request.urlopen(url).read()
            soup = bs4.BeautifulSoup(page_content, features="html.parser")

            page_text = ''

            for paragraph in soup.find_all("p"):
                page_text += paragraph.text

            page_text = re.sub(r'\[.*?\]+', '', page_text)

            content.write(page_text.encode())
            content.close()

    with open(directory_path, 'r') as content_file:
        content_text = (content_file.read()).split()
        content_file.close()

    directory_path = directory_path.replace('\\content.bin', '\\words.txt')

    with open(directory_path, 'w') as words_file:
        for word in content_text:
            words_file.write(word + '\n')
        words_file.close()


wiki_parser('https://en.wikipedia.org/wiki/Winston_Churchill', 'parsers')
