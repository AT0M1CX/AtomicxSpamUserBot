echo Установка..
sleep 0.5
@echo off
pkg update -y
pkg upgrade -y
apt upgrade -y
apt update -y
pkg install python -y
pip install tgcrypto
pip install pyrogram

clear