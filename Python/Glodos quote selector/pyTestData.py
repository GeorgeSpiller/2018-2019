from bs4 import BeautifulSoup
import requests
import os
from playsound import playsound

def sanitizeString(str1):
    garbageChars = "\\'\",!?.[]:;%&*\n"
    for c in garbageChars:
        str1 = str1.replace(c, "")
    str1 = str1.lower()
    str1.strip()
    return str1

def GetPageSoup():
    page = requests.get("https://theportalwiki.com/wiki/GLaDOS_voice_lines")
    print(page)
    return BeautifulSoup(page.content, 'html.parser')

def gen_getlitag():
    liTagList = GetPageSoup().find_all('i')
    for li in liTagList:
        yield li

def GetDownloadUrl(audioName):
    for item in gen_getlitag():
        curr_iTagText = sanitizeString(item.get_text())
        #print(curr_iTagText)
        f = open("SANITISEDTESTDATA.txt", 'a')
        f.write(curr_iTagText)
        f.write("\n")
        f.close()

GetDownloadUrl("")