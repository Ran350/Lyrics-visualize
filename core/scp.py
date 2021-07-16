from core import config

import requests
from bs4 import BeautifulSoup

from sys import exit
from time import sleep


def get_lyrics() -> str:
    ## -----*----- 歌詞を取得（メイン） -----*----- ##
    dir = extract_song_dir(artist=config.ARTIST, song=config.SONG)

    return extract_all_lyrics(dir)


def extract_song_dir(artist: str, song: str) -> list:
    ## -----*----- 曲のディレクトリ部を取得 -----*----- ##
    # 歌手名検索用のURL
    url = config.ARTIST_SEARCHING_URL + artist

    html = download_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    # 表の曲名列のタグ
    song_selector = '#ichiran > div > table > tbody > tr > td.side.td1 > a'
    tags = soup.select(song_selector)

    # 全曲解析
    if song == '*':
        directory = []

        for tag in tags:
            href = tag.get('href')

            # '/song/'を含むhrefのみ
            if '/song/' in href:
                directory.append(href)

            sleep(3)  # 優しさ
            print('*', end='')

        return directory
        # 例: ['/song/12950/',/song/12951/,...]

    for tag in tags:
        if tag.text == song:
            return [tag.get('href')]  # 例: ['/song/12950/']

    print(f'{song} by {artist} was not found')
    exit()


def extract_all_lyrics(directories: list) -> str:
    ## -----*----- すべての歌詞を結合した文字列を取得 -----*----- ##
    lyrics = ''
    for dir in directories:
        lyrics += extract_lyrics(dir)

    return lyrics


def extract_lyrics(directory: str) -> str:
    ## -----*----- 歌詞文字列を取得 -----*----- ##
    url = config.DOMAIN + directory

    html = download_html(url)

    soup = BeautifulSoup(html, 'html.parser')

    selector = '#kashi_area'

    return soup.select_one(selector).text


def download_html(url: str) -> bytes:
    ## -----*----- 指定URLのHTML文字列を取得 -----*----- ##
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.content
    except:
        print('this page is not found')
        exit()
