#!/usr/bin/env bash

echo 'deb http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu precise main' >> /etc/apt/sources.list
echo 'deb-src http://ppa.launchpad.net/v-launchpad-jochen-sprickerhof-de/pcl/ubuntu precise main' >> /etc/apt/sources.list
echo 'deb http://ftp.debian.org/debian experimental main' >> /etc/apt/sources.list
apt-get update
apt-get install -y --force-yes build-essential python-pip pcl-1.5 python-numpy python-dev python-nose
pip install cython
