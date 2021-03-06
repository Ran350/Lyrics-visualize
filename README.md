# Lyrics-visualize
歌詞を可視化したワードクラウド画像を生成するプログラム

# DEMO

![demo](https://github.com/Ran350/Lyrics-visualize/blob/master/image/%E4%B8%B8%E3%81%AE%E5%86%85%E3%82%B5%E3%83%87%E3%82%A3%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF.png?raw=true)

> 曲名:丸の内サディスティック  作詞:椎名林檎

# Requirement

[requirements.txt](./requirements.txt) を参照してください．

# Usage

## Build

```sh
git clone <this repo>
cd <this repo>
pipenv install

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

pipenvで作られた仮想環境へ入って実行する．
```sh
pipenv shell
pipenv run main
```

仮想環境から抜けるときは次を実行する．
```sh
deactivate
exit
```

# References

<https://www.uta-net.com/>

# Author

[Ran350](https://github.com/Ran350)
