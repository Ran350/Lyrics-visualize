from wordcloud import WordCloud
from core import config


def generate(words: list) -> None:
    ## -----*----- wordcloud画像の生成、保存 -----*----- ##
    text = ' '.join(words)     # 単語リストをWordCloud用に整形

    wordcloud = WordCloud(background_color=config.BACKGROUND_COLOR,
                          font_path=config.FONT_PATH,
                          regexp="[\w']+",  # 一文字単語も含む
                          width=config.IMAGE_WIDTH,
                          height=config.IMAGE_HIGHT).generate(text)

    # 画像ファイル名
    if config.SONG == '*':
        image_name = config.ARTIST + '.png'
    else:
        image_name = config.SONG + '.png'

    # word-cloud 画像を保存
    wordcloud.to_file(config.IMAGE_DIR_PATH + image_name)
