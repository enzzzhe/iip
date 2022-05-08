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

    randomHex = (hashlib.md5(url.encode())).hexdigest()
    directoryPath = f"{base_path}/{randomHex}"

    if not os.path.exists(directoryPath):
        print('such base_path doesn\'t exist: creating new one')
        os.makedirs(directoryPath)

    directoryPath = directoryPath + '\\content.bin'

    contentFileExists = file_search_flag(directoryPath)

    if not contentFileExists:
        with open(directoryPath, 'wb') as content:
            pageContent = urllib.request.urlopen(url).read()
            soup = bs4.BeautifulSoup(pageContent, features="html.parser")

            pageText = ''

            for paragraph in soup.find_all("p"):
                pageText += paragraph.text

            pageText = re.sub(r'\[.*?\]+', '', pageText)

            content.write(pageText.encode())
            content.close()

    with open(directoryPath, 'r') as contentFile:
        contentText = (contentFile.read()).split()
        contentFile.close()

    directoryPath = directoryPath.replace('\\content.bin', '\\words.txt')

    with open(directoryPath, 'w') as wordsFile:
        for word in contentText:
            wordsFile.write(word + '\n')
        wordsFile.close()


wiki_parser('https://en.wikipedia.org/wiki/Winston_Churchill', 'parsers')
