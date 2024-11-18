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

config = {
  "user": "admin",
  "dbName": "data.json"
}

def updateUser():
    try:
        with open(config["dbName"], 'r') as file:
            data = json.load(file)  # Read and load the JSON file
            config["user"] = data["Author"]
          file.close()
    except FileNotFoundError:
        print("Error: JSON file not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON file.")
        sys.exit(1)

def function(str, args):
    command_functions[str](str, args)
  
def notFunction(str, args):
    return False

decision = {
    True: function,
    False: notFunction
}

def input_():
    updateUser()
    inp = input(colortext(config["user"], "yellow") + colortext(" ~ ", "green"))
    split = inp.split(" ")
    args = []
    check = (split[0] in command_functions) or False
    for x in range(len(split)):
        args.append(split[x].lower())
    decision[check](split[0], args)
    input_()

input_()
