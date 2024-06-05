import os
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from pycda.config import USER_AGENT, QUALITIES


class PyCDA:
    def __init__(self, url):
        self.__url = url
        self.__quality_urls = {q: f'/vfilm?wersja={q}p' for q in QUALITIES}

        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument('headless')
        self.__options.add_argument(f'user-agent={USER_AGENT}')
        self.__driver = webdriver.Chrome(options=self.__options)
        self.__soup = self.__get_soup(url)

    def __get_soup(self, url):
        self.__driver.get(url)
        page_src = self.__driver.page_source
        self.__driver.quit()
        return BeautifulSoup(page_src, 'html.parser') if page_src else None

    def thumbnail(self) -> str:
        thumbnail_url = self.__soup.find('meta', {'property': 'og:image'}).get('content')
        if thumbnail_url:
            return thumbnail_url
        else:
            raise Exception('Thumbnail url could not be fetched')

    def title(self) -> str:
        title = self.__soup.find('meta', {'property': 'og:title'}).get('content')
        if title:
            return title
        else:
            raise Exception('Title could not be fetched')

    def __get_video_src(self, quality):
        soup = self.__get_soup(self.__url + self.__quality_urls[quality])
        if soup:
            video_tag = soup.find('video', class_='pb-video-player')
            if video_tag:
                return video_tag.get('src')
        return None

    def __find_best_quality(self):
        for quality in QUALITIES:
            target = self.__get_video_src(quality)
            if target and len(target.split('/')[-1]) > 4:
                return target
        return None

    def download(self, filename='../downloads/cda_file.mp4', on_progress_callback=None):
        target = self.__find_best_quality()
        if target:
            print(f"Found video URL: {target}")
            if not os.path.exists(filename):
                print('Downloading...')
                urllib.request.urlretrieve(target, filename, reporthook=on_progress_callback)
            else:
                print('File already downloaded')
        else:
            print("No valid video URL found.")
