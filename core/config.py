# input
ARTIST: str = '椎名林檎'
SONG: str = '丸の内サディスティック'  # 全曲解析: '*'
IS_REMOVE_TITLE: bool = False


# scraping
DOMAIN: str = 'https://www.uta-net.com/'
ARTIST_SEARCHING_URL: str = DOMAIN + 'search/?Aselect=1&Bselect=4&sort=4&Keyword='

# dictionary config
DICTIONARY_PATH: str = '/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
# DICTIONARY_PATH: str = '-Ochasen'

# stop words config
STOP_WORDS_PATH: str = './config/stop_words.csv'

# word-cloud config
FONT_PATH: str = '/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf'
IMAGE_WIDTH: int = 800
IMAGE_HIGHT: int = 600
BACKGROUND_COLOR: str = 'white'
IMAGE_DIR_PATH: str = './image/'
