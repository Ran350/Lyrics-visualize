import MeCab
import csv
from core import config


def get_words(lyrics: str) -> list:
    ## -----*----- 歌詞から単語を取得(メイン) -----*----- ##
    mecab = set_nlp()

    stop_words = get_stop_words()  # 除外単語を取得

    if config.IS_REMOVE_TITLE:
        add_title_to_stopwords(stop_words, mecab)

    # 形態素解析
    return separate_lyrics_into_words(lyrics, mecab, stop_words)


def set_nlp():
    ## -----*----- MeCab解析器の準備 -----*----- ##
    # 解析器の設定
    dictionary = '-d ' + config.DICTIONARY_PATH
    mecab = MeCab.Tagger(dictionary)

    mecab.parse('')  # これでUnicodeDecodeErrorを避けられるらしい

    return mecab


def get_stop_words() -> list:
    ## -----*----- 除外単語を取得 -----*----- ##
    with open(config.STOP_WORDS_PATH) as f:
        for row in csv.reader(f):
            return row


def add_title_to_stopwords(stop_words: list, mecab: MeCab.Tagger):
    ## -----*----- 曲名を除外リストに追加 -----*----- ##
    node = mecab.parseToNode(config.SONG)  # 曲名を分かち書きしてノードに

    while node:
        word = node.surface  # 単語
        stop_words.append(word)
        node = node.next


def separate_lyrics_into_words(lyrics: str,  mecab: MeCab.Tagger, stop_words: list) -> list:
    ## -----*----- 歌詞を分かち書き -----*----- ##
    node = mecab.parseToNode(lyrics)  # 分かち書きしてノードに

    word_list = []

    # 条件に合うかを一単語ずつ調べる
    while node:
        term = node.surface  # 単語

        word_type = node.feature.split(',')
        # word_type: [品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音]

        if (word_type[0] in ['名詞', '形容詞', '副詞', '動詞', '感動詞', '接続詞'] and  # 品詞を選択
            word_type[1] not in ['接尾', '非自立'] and  # <-を除外
            word_type[2] not in ['助動詞語幹'] and  # <-を除外
            word_type[4] not in ['サ変・スル'] and  # サ変動詞を除外
                term not in stop_words):
            word_list.append(term)

        node = node.next

    return word_list
