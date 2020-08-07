# Name (Lyrics-visualize)

任意のアーティストの任意の曲を入力すると、
その歌詞を取得し、
歌詞を形態素分析して、
単語をその出現頻度に応じた大きさで並べた画像を出力する
プログラム

# DEMO

![demo_image](/image/丸の内サディスティック.png)

> 曲名:丸の内サディスティック　作詞:椎名林檎

# Requirement

- Python 3.7

- requests 2.22.0
- beautifulsoup4 4.8.2
- mecab-python3 0.996.5
- wordcloud 1.6.0

# Usage

## Build

```bash
git clone https://github.com/Ran350/Lyrics-visualize
cd /home/..../Lyrics-visualize/main.py
```

## Input

実行ファイル main.py 中の、ARTISTS_NAME に歌手名を、SONG_NAME に曲名を入力する。
曲名を除外して出力したい場合には、is_remove_title を'yes'にする。

```
ARTISTS_NAME = '椎名林檎'
SONG_NAME = '丸の内サディスティック'  # 全曲解析したいときは*を入力
is_remove_title = 'yes'  # 曲名は除外して出力するか yes/no
```

> main.py

## Run

```bash
python main.py
```

# References

<https://www.uta-net.com/>

# Author

- Ran350
