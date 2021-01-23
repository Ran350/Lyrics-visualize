import scp
import nlp
import wc


def main():
    artist = '椎名林檎'
    song = '丸の内サディスティック'  # 全曲解析 -> '*'を入力
    is_remove_title = False  # 曲名を除外して出力 -> True

    # 歌詞の取得
    lyrics = scp.get_lyrics(artist_name=artist, song_name=song)
    print(lyrics)

    # 形態素分析して単語選択
    word_list = nlp.get_words(lyrics=lyrics,
                              title=song,
                              is_rm_title=is_remove_title)
    print(word_list)

    # wordcloud画像の生成と保存
    wc.generate_wc(word_list, artist=artist, title=song)


if __name__ == '__main__':
    main()
