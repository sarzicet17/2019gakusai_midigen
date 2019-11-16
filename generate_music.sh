#!/usr/bin/bash

if [ $# -ne 4 ]; then
  echo "引数は4個必要です" 1>&2
  exit 1
fi
docker run -it --rm magenta python /2019gakusai/generate_midi.py $1 $2 $3 $4
docker run -it --rm timidity midi-convert.sh $4
