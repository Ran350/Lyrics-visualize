import scraping
import nlp
import wc


ARTISTS_NAME = '椎名林檎'
SONG_NAME = '丸の内サディスティック'  # 全曲解析したいときは*を入力
is_remove_title = 'yes'  # 曲名は除外して出力するか yes/no

url = 'https://www.uta-net.com/search/?Aselect=1&Keyword=' + \
    ARTISTS_NAME+'&Bselect=1&sort=4&pnum=1'
base_url = 'https://www.uta-net.com'   # 曲ページの先頭アドレス

rm_wd_list = ['ない', 'ある', 'なっ', 'あっ']  # 意味をなさないような単語を除外


if __name__ == '__main__':
    # 歌詞の取得
    lyrics = scraping.get_lyrics(ARTISTS_NAME, SONG_NAME, url, base_url)

    # 形態素分析して単語選択
    word_list = nlp.get_word_list(
        lyrics, SONG_NAME, rm_wd_list, is_remove_title)

    # wordcloud画像の出力
    wc.generate_wc(word_list, ARTISTS_NAME, SONG_NAME)
