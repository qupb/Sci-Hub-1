'''
This is a test file to check if
every module works.
I could have written this off in 10 lines
but Codacy wanted my imported modules to
do something.
'''
from __future__ import print_function
import platform

print()

# Python 2.x incompatibility
if int(platform.python_version_tuple()[0]) < 3:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 test.py\n")
    print("*"*30 + "\n" + "\tTEST FAILED" + "\n" + "*"*30)
    quit()

if platform.system() not in ['Linux', 'Darwin']:
    print("Looks like you are not running on GNU/Linux or a Mac")
    print("If this test is successful then you can run: ")
    print("\npython3 sci_hub.py\n")

print("This is a test file and does nothing.")

try:
    import argparse
    import os
    import re
    import time
    import webbrowser
except(ImportError):
    print("Either argparse, os platform, time, webbrowser"
          + "or re could not be imported")
    quit()

try:
    from bs4 import BeautifulSoup as bs
    import requests
except(ImportError):
    print("Either requests or BeautifulSoup could not be imported")
    quit()

parser = argparse.ArgumentParser(description="The most useless python script \
                                              written by me")
parser.add_argument("target", help="enter any random URL")
args = parser.parse_args()

print("\n" + "*"*50 + "\n" + "YOUR TEST IS ALREADY SUCCESSFUL")
print("The next output is to satisfy Codacy :/\n")
print("You can safely ignore the output next\n" + "*"*50 + "\n")
time.sleep(5)

print(os.listdir("./"))
print(platform.system())

print(args)
response = requests.get(args.target)
if response.status_code == requests.codes.ok:
    soup = bs(response.content, "lxml")
    print(soup.title.text)
else:
    print("Something happened")

if re.match("oir", "air"):
    print("yes")

print("\nNow your default web browser will open")
print("Don't be scared, I haven't hacked your computer :P\n")
print("If it doesn't then try setting a default browser"
      + "for the script to work properly")
time.sleep(2)
webbrowser.open_new("https://google.com")
