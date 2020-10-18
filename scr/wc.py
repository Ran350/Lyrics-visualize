from wordcloud import WordCloud


def generate_wc(word_list,  ARTISTS_NAME, SONG_NAME):
    ## -----*----- wordcloud画像の生成、保存 -----*----- ##
    '''
    word_list : 出力単語
    SONG_NAME : 曲名
    ARTISTS_NAME : 歌手名
    '''
    text = ' '.join(word_list)     # 形態素解析された単語のリストをWordCloud用に処理

    # フォントを指定
    fpath = "/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf"    # 日本語フォントのパス

    wordcloud = WordCloud(background_color="white", font_path=fpath,
                          regexp="[\w']+", width=800, height=600).generate(text)

    # 画像に名前をつける
    if SONG_NAME == '*':
        image_name = ARTISTS_NAME + '.png'
    else:
        image_name = SONG_NAME + '.png'

    # 画像を保存
    wordcloud.to_file('./image/'+image_name)   # WordCloudの画像を保存
