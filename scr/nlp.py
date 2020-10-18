import MeCab


def set_nlp():
    ## -----*----- MeCabを準備 -----*----- ##
    # mecab-ipadic-NEologdのパスを指定 (Web上の新語をデフォルトの辞書に追加したもの)
    mecab = MeCab.Tagger(
        '-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
    # mecab = MeCab.Tagger('-Ochasen')   #デフォルトの辞書

    mecab.parse('')  # 文字列がGCされるのを防ぐ

    return mecab


def remove_word(mecab, SONG_NAME, rm_wd_list):
    ## -----*----- 曲名を除外リストに追加 -----*----- ##
    title_node = mecab.parseToNode(SONG_NAME)  # 分けてノードごとにする

    while title_node:
        term = title_node.surface  # 単語
        word_type = title_node.feature.split(",")
        rm_wd_list.append(term)
        title_node = title_node.next

    return word_type


def get_word_list(kashis, SONG_NAME, rm_wd_list, is_remove_title):
    ## -----*----- 形態素分析して単語選択(メイン) -----*----- ##
    '''
    lyrics : 歌詞文字列
    SONG_NAME : 曲名
    stoplist : 除外単語リスト
    is_remove_title
    '''
    word_list = []  # 抽出後の文字列を入れる

    mecab = set_nlp()

    # 曲名を除外リストに追加
    if is_remove_title == 'yes':
        word_type = remove_word(mecab, SONG_NAME, rm_wd_list)

    # 品詞に分解して、特定の品詞を抽出
    node = mecab.parseToNode(kashis)  # 分けてノードごとにする
    while node:
        term = node.surface  # 単語
        word_type = node.feature.split(",")
        # print(word_type)
        # 形容詞,副詞,感動詞,接続詞,名詞(非自立以外),動詞(サ変以外)を抽出
        if word_type[0] in ["名詞", "形容詞", "副詞", "動詞", "感動詞", "接続詞"]:  # 品詞を選択
            if word_type[4] not in ["サ変・スル"]:  # 動詞のサ変を除外
                if word_type[1] not in ["接尾"]:  # 接尾辞を除外
                    if word_type[2] not in ["助動詞語幹"]:  # 助動詞を除外
                        if word_type[1] not in ["非自立"]:  # 非自立名詞を除外
                            if term not in rm_wd_list:  # 意味のない単語を除外
                                # if not term.isdigit():  # 数字を除外
                                word_list.append(term.upper())
        node = node.next

    print(word_list)

    return word_list
