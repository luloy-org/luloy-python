import time
import sys
import phonenumbers
import colorama
import json
import requests
import socket
import os
import tabulate
import re
import pyptools
import subprocess

dbName = 'data.json'
from pyptools import *
from colorama import Fore, Back, Style
from phonenumbers import timezone,geocoder,carrier
from tabulate import tabulate

def Func1(args):
  print(Fore.RED + Back.GREEN + 'Function called' + Style.RESET_ALL)
  
def numberInfo (args):
  table=[]
  print("input phonenumber, with country code")
  print("Example: +63xxxxxxxxxx")
  num=input(Fore.GREEN+">> "+Style.RESET_ALL)
  phone = phonenumbers.parse(num)
  time = timezone.time_zones_for_number(phone)
  carry = carrier.name_for_number(phone,"en")
  country = geocoder.description_for_number(phone,"en")
  
  print(phone)
  print(time)
  print(carry)
  print(country)
  
def searCH(table,str):
  if (isinstance(table,(set,list))==True):
    suspected=[]
    for x in table:
      if (re.search(str,x)!=None):
        suspected.append(x)
    return suspected
  else:
    return None
    

def viewData (args):
  check = (len(args)>=2) or False
  answer=input("New author: ")
  if (answer!=""):
    newuser=None
    with open(dbName, 'r+') as file:
      data = json.load(file)
      data["Author"] = answer
      newuser=answer
      file.seek(0)
      json.dump(data, file, indent=4)
      file.truncate
      print(data["Author"])
      file.close()
      log(f"username changed to {newuser}")
  else:
      print(colortext("Missing argument 1","red"))
    
def viewAuthor (args):
  with open(dbName, 'r') as f:
    data = json.load(f)
    f.close()
    return data["Author"]
    
def showauthor (args):
  get=viewAuthor({})
  text=f"Current user: {colortext(get,"yellow")}"
  print(text)


def get_ip_info(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main(args):
    answer=input("Input ip address: ")
    if (answer!=""):
      
       # Replace with the IP address you want to look up
      info = get_ip_info(answer)
      if info:
        print(f"IP Address: {info.get('ip')}")
        print(f"Hostname: {info.get('hostname')}")
        print(f"City: {info.get('city')}")
        print(f"Region: {info.get('region')}")
        print(f"Country: {info.get('country')}")
        print(f"Location: {info.get('loc')}")
        print(f"Organization: {info.get('org')}")
        print(f"Timezone: {info.get('timezone')}")
      else:
        print("Failed to get information for the given IP address.")
    else:
      print(Fore.RED+"No ip input"+Style.RESET_ALL)

def get_local_ip(args):
    hostname = socket.gethostname()  # Get the hostname of the machine
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)# Get the IP address associated with the hostname
    return local_ip

def get_public_ip(args):
    response = requests.get('https://api.ipify.org?format=json')  # Call an external service to get the public IP address
    public_ip = response.json().get('ip')
    print(public_ip)
    return public_ip

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Local IP Address: {local_ip}")
    try:
        public_ip = get_public_ip()
        print(f"Public IP Address: {public_ip}")
    except Exception as e:
        print(f"Could not retrieve public IP: {e}")
      
def list_of_functions(args):
  table = []
  for i in functions:
    funcText = Fore.YELLOW + functions[i]["function"].__name__ +'()'+Style.RESET_ALL
    table.append([i,funcText])
    
  finishProduct=tabulate(table,headers=['Command Name', 'Function'], tablefmt='orgtbl')
  print(finishProduct)

def color_text (args):
  put=input('color: red,green,yellow,magenta\n>')
  text=input("text: ")
  bold=input("bold: 1=yes,2=no\n")
  colored=colortext(text,put.lower())
  if (bold=="1"):
    colored=boldtext(colored)
  print(colored)

def getUserInfo (args):
  iD = input('Roblox id: ')
  x = requests.get("https://users.roblox.com/v1/users/"+iD)
  for i in x.json():
    print(colortext(i,"green")+": "+str(x.json()[i]))
    
def readcontent(args):
  ans = input("Enter file name: ")
  with open(ans, "r") as file:
    print(file.read())
    
def viewlogs (args):
  with open("data.json", "r") as file:
    data=json.load(file)
    count=1
    for x in data["Logs"]:
      text=f"[{colortext(f"{x["logdate"]}","green")}]:{x["logtext"]}"
      print(text)
      count+=1
  
functions = {
  "testfunc":{
    "function": Func1,
    "des": "This is the first function for test"
  },
  "viewlogs":{
    "function": viewlogs,
    "des": "View system logs"
  },
  "numberinfo":{
    "function": numberInfo
  },
  "c-author": {
    "function": viewData
  },
  "v-author": {
    "function": showauthor
  },
  "get_ip_info": {
    "function": main
  },
  "my_public_ip": {
    "function": get_public_ip
  },
  "my_private_ip": {
    "function": get_local_ip
  },
  "f-list": {
    "function": list_of_functions
  },
  "colored-t": {
    "function": color_text
  },
  "roblox_user_info":{
    "function": getUserInfo
  },
  "view_content":{
    "function": readcontent
  }
}
