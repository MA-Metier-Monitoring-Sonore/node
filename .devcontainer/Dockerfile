FROM python:3.14-bookworm

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libasound2-dev alsa-utils libasound2-plugins pulseaudio-utils

WORKDIR /root

RUN wget http://ftp.ch.debian.org/debian/pool/main/g/git-flow/git-flow_1.12.3-3_all.deb \
    && dpkg -i git-flow_1.12.3-3_all.deb \
    && rm git-flow_1.12.3-3_all.deb