import requests
import bs4
import re
from sys import exit
from time import sleep


def load(url):
    ## -----*----- 指定URLのHTML文字列を取得 -----*----- ##
    try:
        res = requests.get(url)
        res.raise_for_status()
    except:
        print('this page is not found')
    return res.text


def pickup_tag(html, find_tag):
    ## -----*----- すべての指定タグを取得 -----*----- ##
    soup = bs4.BeautifulSoup(str(html), 'html.parser')
    paragraphs = soup.find_all(find_tag)

    return paragraphs


def remove_tags(html):
    ## -----*----- 日本語以外の文字列を除去 -----*----- ##
    soup = bs4.BeautifulSoup(str(html), 'html.parser')
    # htmlタグの除去
    kashi_row = soup.getText()
    kashi_row = kashi_row.replace('\n', '')
    kashi_row = kashi_row.replace('　', '')

    # 英数字の排除
    kashi_row = re.sub(r'[a-zA-Z0-9]', '', kashi_row)
    # 記号の排除
    kashi_row = re.sub(r'[ ＜＞♪`‘’“”・…_！？!-/:-@[-`{-~]', '', kashi_row)
    # 注意書きの排除
    kashi = re.sub(r'注意：.+', '', kashi_row)

    return kashi


def get_lyrics(ARTISTS_NAME, SONG_NAME, url, base_url):
    ## -----*----- 歌詞を取得（メイン） -----*----- ##
    '''
    ARTISTS_NAME : 歌手名
    SONG_NAME : 曲名
    url : アーティストページのURL
    base_url : uta-net.comのURL
    '''

    html = load(url)    # ページの取得

    musics_url = []  # 曲ごとのurl
    kashis = ''  # 歌詞

    # 歌手ページURLの取得
    i = 0
    # td要素の取り出し
    for td in pickup_tag(html, 'td'):
        # a要素の取り出し
        for a in pickup_tag(td, 'a'):
            # 全曲解析
            if SONG_NAME == '*':
                if 'song' in a.get('href'):
                    musics_url.append(base_url + a.get('href'))    # urlを配列に追加
            # １曲だけを解析
            if SONG_NAME == a.text:
                if 'song' in a.get('href'):  # href属性にsongを含むか
                    musics_url.append(base_url + a.get('href'))    # urlを配列に追加
                    i += 1
                    break
        if i == 1:
            break

    # 曲が見つからなかった場合、プログラムを終了
    if musics_url == []:
        print(SONG_NAME + " by " + ARTISTS_NAME + " is not found")
        exit()

    print(musics_url)  # for debug

    # 歌詞の取得
    for i, page in enumerate(musics_url):
        print('{}曲目:{}'.format(i + 1, page))
        html = load(page)

        for div in pickup_tag(html, 'div'):
            div = str(div)  # id検索がうまく行えなかった為、一度strにキャスト

            if r'itemprop="text"' in div:   # 歌詞が格納されているdiv要素か
                kashi = remove_tags(div)  # 不要なデー(タグなど)タを取り除く
                print(kashi, end='\n\n')  # for debug
                kashis += kashi + '\n'  # 歌詞を１つにまとめる
                sleep(1)
                break

    return kashis
