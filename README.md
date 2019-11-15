# 2019大学祭用ファイル(magentaのdockerイメージを使用)
## ディレクトリ構成
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
### MIDIファイルの作成
上記コマンド実行後コンテナに入り,

```python /2019gakusai/generate_midi.py 引数```

を実行する(引数の数は4つ Red Green Blue ファイル名)

実行例:

```# python /2019gakusai/generate_midi.py 30 40 30 muse1.mid ```

実行後，output_midiディレクトリの中にMIDIデータが生成される

***
Googleの機械学習を用いたアートフレームワークであるmagentaのDockerイメージを使用しています

