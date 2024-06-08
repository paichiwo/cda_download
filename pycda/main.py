import os
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from pycda.helpers import format_date_string, format_duration


class PyCDA:
    """Lightweight CDA wrapper"""

    def __init__(self, url: str):
        self.__url = url
        self.__qualities = ['1080', '720', '480', '360']
        self.__quality_urls = {q: f'/vfilm?wersja={q}p' for q in self.__qualities}

        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument('headless')
        self.__options.add_argument(f'user-agent={UserAgent().random}')

        self.__driver = webdriver.Chrome(options=self.__options)
        self.__soup = self.__get_soup(url)

    def __get_soup(self, url: str) -> BeautifulSoup:
        # Return page source in the form of beautiful soup
        self.__driver.get(url)
        page_src = self.__driver.page_source
        return BeautifulSoup(page_src, 'html.parser') if page_src else None

    def thumbnail(self) -> str:
        # Fetch thumbnail url
        thumbnail_url = self.__soup.find('meta', {'property': 'og:image'}).get('content')
        if thumbnail_url:
            return thumbnail_url
        else:
            raise Exception('Thumbnail url could not be fetched')

    def title(self) -> str:
        # Fetch video title
        title = self.__soup.find('meta', {'property': 'og:title'}).get('content')
        if title:
            return title
        else:
            raise Exception('Title could not be fetched')

    def publish_date(self) -> str:
        # Fetch video publish date
        date = self.__soup.find('meta', {'itemprop': 'uploadDate'}).get('content')
        if date:
            return format_date_string(date)
        else:
            raise Exception('Publish date could not be fetched')

    def duration(self) -> str:
        # Fetch video duration
        duration = self.__soup.find('meta', {'itemprop': 'duration'}).get('content')
        if duration:
            return format_duration(duration)
        else:
            raise Exception('Duration could not be fetched')

    def filesize(self) -> int:
        # Fetch video file size
        target = self.__find_best_quality()
        if target:
            request = urllib.request.Request(target, method='HEAD')
            response = urllib.request.urlopen(request)
            return int(response.headers.get('Content-Length'))
        else:
            raise Exception('Filesize could not be fetched')

    def description(self) -> str:
        # Fetch video description
        description = self.__soup.find('meta', {'itemprop': 'description'}).get('content')
        if description:
            return description
        else:
            raise Exception('Description could not be fetched')

    def __get_video_src(self, quality: str):
        # Fetch video target
        soup = self.__get_soup(self.__url + self.__quality_urls[quality])
        if soup:
            video_tag = soup.find('video', class_='pb-video-player')
            if video_tag:
                return video_tag.get('src')
        return None

    def __find_best_quality(self):
        # Find the best quality of the available video sources
        for quality in self.__qualities:
            target = self.__get_video_src(quality)
            if target and len(target.split('/')[-1]) > 4:
                return target
        return None

    def download(self, filename: str = None, on_progress_callback=None):
        # Download target
        target = self.__find_best_quality()
        if target:
            output_filename = f'{filename if filename else self.title()}.mp4'
            if not os.path.exists(output_filename):
                print('Downloading...')
                urllib.request.urlretrieve(target, output_filename, reporthook=on_progress_callback)
            else:
                print('File already downloaded')
        else:
            print('No valid video URL found.')
