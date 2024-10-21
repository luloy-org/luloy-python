

import json
import time, sys
import phonenumbers
import colorama
import fontstyle
import datetime

from colorama import Fore, Back, Style

def colortext(text, color):
	colorList={
	"red": Fore.RED,
	"yellow": Fore.YELLOW,
	"green": Fore.GREEN,
	"magenta": Fore.MAGENTA,
	"cyan": Fore.CYAN
	}
	if (color in colorList):
		return colorList[color]+text+Style.RESET_ALL
	else:
		None
		
def boldtext(text):
	return fontstyle.apply(text, 'bold')

def log (text):
	date = datetime.datetime.now()
	with open('data.json','r+') as file:
		data=json.load(file)
		loglist=data["Logs"]
		loglist.append({"logdate":f"{date}","logtext":text})
		file.seek(0)
		json.dump(data, file, indent=4)
		file.truncate
		file.close()
		
