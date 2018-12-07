#!/bin/bash
#
if ! sudo netstat -tnlp | grep 8818 &> /dev/null; then
    cd /home/rocketchat/
    /usr/local/bin/docker-compose up -d
fi

