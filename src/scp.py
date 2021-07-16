import requests
from bs4 import BeautifulSoup
import re
from sys import exit
from time import sleep


def get_lyrics(artist_name: str, song_name: str) -> str:
    ## -----*----- 歌詞を取得（メイン） -----*----- ##
    dir = extract_song_dir(artist=artist_name, song=song_name)

    return extract_all_lyrics(dir)


def extract_song_dir(artist, song) -> list:
    ## -----*----- 曲のディレクトリ部を取得 -----*----- ##
    # 歌手名検索用のURL
    url = 'https://www.uta-net.com/search/?Aselect=1&Bselect=4&sort=4&Keyword='+artist

    html = download_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    # 表の曲名列のタグ
    song_selector = '#ichiran > div > table > tbody > tr > td.side.td1 > a'
    tags = soup.select(song_selector)

    if song == '*':
        hrefs = [t.get('href') for t in tags]
        return [h for h in hrefs if '/song/'in h]  # '/song/'を含むhrefのみ
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
    domain = 'https://www.uta-net.com'
    url = domain + directory

    html = download_html(url)

    soup = BeautifulSoup(html, 'html.parser')

    selector = '#kashi_area'
    content = soup.select_one(selector).text

    return normalize_lyrics(content)


def normalize_lyrics(cont: str) -> str:
    ## -----*----- 歌詞文字列の正規化 -----*----- ##
    cont = re.sub(r'注意：.+', '', cont)  # 注釈を除去
    cont = re.sub(r'^亜-熙ぁ-んァ-ヶa-zA-Z ', '', cont)  # 日本語,アルファベット,空白のみ抽出

    return cont


def download_html(url: str) -> bytes:
    ## -----*----- 指定URLのHTML文字列を取得 -----*----- ##
    try:
        sleep(3)  # 優しさ
        res = requests.get(url)
        res.raise_for_status()
        return res.content
    except:
        print('this page is not found')
