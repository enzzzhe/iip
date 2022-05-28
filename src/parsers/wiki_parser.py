"""System module."""
import hashlib
import urllib.request
import bs4
import os
import re


def counter(my_text, word):
    """Searching for words with map"""
    return sum(map(lambda x:x == word, my_text))

def url_search(url):
    """Searching for url.txt file """
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
    """Searching for content.bin file"""
    if os.path.exists(path):
        print('content.bin has been found')
        return True
    else:
        print('content.bin hasn\'t been found in directory: creating new one')
        return False


def wiki_parser(url: str, base_path: str):
    """Wiki parser"""
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

            #content.write(soup)
            # суп2 для выделения ссылок
            soup2 = soup
            page_urls = ''
            page_text = ''

            for paragraph in soup.find_all("p"):
                page_text += paragraph.text

            for paragraph in soup2.find_all("a"):
                temporary = paragraph.get('href', None)
                if temporary is not None:
                    page_urls = page_urls + ' ' + temporary

            page_urls = page_urls.split()
            page_urls1 = []

            for current_url in page_urls:
                if not current_url.find('wikipedia.org') == -1:
                    page_urls1.append(current_url)

            page_text = re.sub(r'\[.*?\]+', '', page_text)

            content.write(page_text.encode())
            content.close()
    else:
        with open(directory_path, 'wb') as content:
            page_content = urllib.request.urlopen(url).read()
            soup = bs4.BeautifulSoup(page_content, features="html.parser")

            content.write(soup)
            # суп2 для выделения ссылок
            soup2 = soup
            page_text = ''
            page_urls = ''

            for paragraph in soup.find_all("p"):
                page_text += paragraph.text

            for paragraph in soup2.find_all("a"):
                temporary = paragraph.get('href', None)
                if temporary is not None:
                    page_urls = page_urls + ' ' + temporary

            page_urls = page_urls.split()
            page_urls1 = []

            for current_url in page_urls:
                if not current_url.find('wikipedia.org') == -1:
                    page_urls1.append(current_url)


            page_text = re.sub(r'\[.*?\]+', '', page_text)

            content.write(page_text.encode())


    with open(directory_path, 'r') as content_file:
        content_text = (content_file.read())
        content_file.close()

    directory_path = directory_path.replace('\\content.bin', '\\words.txt')

    content_text = content_text.replace(',', '')
    content_text = content_text.replace('.', '')
    content_text = content_text.replace('?', '')
    content_text = content_text.replace('!', '')
    content_text = content_text.replace('(', '')
    content_text = content_text.replace(')', '')
    content_text = content_text.replace(':', '')
    content_text = content_text.replace('"', '')
    content_text = content_text.replace('\'', '')
    content_text = content_text.lower()
    content_text = content_text.split()

    dictionary = {}
    for line in content_text:
        dictionary[line] = counter(content_text, line)
    #print(dictionary)


    directory_path = directory_path.replace('\\content.bin', '\\words.txt')


    with open(directory_path, 'w') as words_file:
        for key, value in dictionary.items():
            words_file.write('%s : %s \n' % (key, value))
        words_file.close()

    print(page_urls1)
    return page_urls1



link = input()
directory_name = input()
wiki_parser(link, directory_name)

#https://en.wikipedia.org/wiki/Isaac_Newton
