# 2019大学祭用ファイル(magentaのdockerイメージを使用)
## ディレクトリ構成
###
 ```Dockerfile-magenta #Dockerfile
generate_midi.py #MIDIファイル生成用のスクリプト
output_midi #MIDIファイル出力ディレクトリ(gitの追跡から除外)
 ```
### イメージのビルド
```
docker-compose up --build
```

### コンテナに入る
```
docker-compose run magenta
```
## MIDIファイルの作成
### コンテナに入り,
```
python generate_midi.py 引数
```
### を実行するとoutput_midiディレクトリにMIDIファイルが出力される

### Googleの機械学習を用いたアートフレームワークであるmagentaのDockerイメージを使用しています

