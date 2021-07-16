from wordcloud import WordCloud


def generate_wc(words: list,  artist: str, title: str):
    ## -----*----- wordcloud画像の生成、保存 -----*----- ##

    text = ' '.join(words)     # 単語リストをWordCloud用に整形

    # フォントを指定
    fpath = '/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf'

    wordcloud = WordCloud(background_color='white',
                          font_path=fpath,
                          regexp="[\w']+",  # 一文字単語も含む
                          width=800,
                          height=600).generate(text)

    # 画像ファイル名
    if title == '*':
        image_name = artist + '.png'
    else:
        image_name = title + '.png'

    # 画像を保存
    wordcloud.to_file('./image/'+image_name)   # WordCloudの画像を保存
