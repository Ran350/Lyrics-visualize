from core import scp
from core import nlp
from core import wc

from core import config


def main():
    # 歌詞の取得
    lyrics = scp.get_lyrics()
    print(lyrics)

    # 形態素分析して単語選択
    word_list = nlp.get_words(lyrics=lyrics)
    print(word_list)

    # wordcloud 画像の生成と保存
    wc.generate(word_list)


if __name__ == '__main__':
    main()
