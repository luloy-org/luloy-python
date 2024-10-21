import json
import time, sys
import phonenumbers
import functionsModule
import dataModule
import colorama
import pyptools

from colorama import Fore, Back, Style
from dataModule import command_functions
from pyptools import *

config={
  "user": "admin",
  "dbName": "data.json"
}

def updateUser():
  with open("data.json", 'r') as file:
    file.seek(0)
    data=json.load(file)
    config["user"] = data["Author"]
    file.close()

def function(str, args):
  command_functions[str](str, args)
  
def notFunction(str, args):
  return False

decision={
  True: function,
  False: notFunction
}
def input_():
  updateUser()
  inp = input(colortext(config["user"],"yellow")+colortext(" ~ ","green"))
  split = inp.split(" ")
  args=[]
  check=(split[0] in command_functions) or False
  for x in range(len(split)):
  	args.append(split[x].lower())
  decision[check](split[0], args)
  input_()
    
    
input_()
