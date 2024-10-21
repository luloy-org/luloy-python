
#! /bin/bash
light_green='\e[1;32m'
yellow='\e[33m'
nc='\e[0m'

echo -e "${light_green}---Installing Packages---${nc}"

pip install phonenumbers
pip install tabulate
pip install colorama
pip install requests
pip install Flask
pip install fontstyle


clear
echo -e "${light_green}Installation Finished, program started!${nc}"

python3 index.py




