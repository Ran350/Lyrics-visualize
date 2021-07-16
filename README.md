# Lyrics-visualize
歌詞を可視化したワードクラウド画像を生成するプログラム

# DEMO

![demo_image](image/丸の内サディスティック.png)

> 曲名:丸の内サディスティック  作詞:椎名林檎

# Requirement

[requirements.txt](./requirements.txt) を参照してください．

# Usage

## Build

```sh
git clone <this repo>
cd <this repo>
pip install -r requirements.txt
```

## Input

[core/config.py](core/config.py) で以下を設定する．

歌手名と曲名を設定する．
```py
ARTIST: str = '椎名林檎'
SONG: str = '丸の内サディスティック'  # 全曲解析: '*'
IS_REMOVE_TITLE: bool = False
```

形態素解析に用いる辞書のパスを指定する．
辞書をインストールしていない場合は，コメントアウトを外して`-Ochasen`を指定する．

```py
DICTIONARY_PATH: str = '/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
# DICTIONARY_PATH: str = '-Ochasen'
```

ワードクラウド画像で用いるフォントのパスを指定する．

```py
FONT_PATH: str = '/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf'
```

## Run

```sh
python main.py
```

# References

<https://www.uta-net.com/>

# Author

- Ran350
