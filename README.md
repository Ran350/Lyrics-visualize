# Name (Lyrics-visualize)

任意のアーティスト名と曲名を入力すると，
歌詞をスクレイピング -> 形態素分析 -> word cloud 画像を生成するプログラム

# DEMO

![demo_image](scr/image/丸の内サディスティック.png)

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
git clone <this repo>
cd <this repo>
```

## Input

実行ファイル main.py 中の， 変数 artist に歌手名を，変数 song に曲名を入力する．
曲名を除外して出力したい場合には，is_remove_title には True を入力する．

```
artist = '椎名林檎'
song = '丸の内サディスティック'  # 全曲解析 -> '*'を入力
is_remove_title = False  # 曲名を除外して出力 -> True
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
