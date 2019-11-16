FROM ubuntu:18.04
MAINTAINER sarzicet17
RUN apt-get update 
RUN apt-get install -y timidity freepats fluid-soundfont-gm fluid-soundfont-gs
RUN mkdir /wavfiles
RUN mkdir /script
COPY midi-convert.sh /script/
