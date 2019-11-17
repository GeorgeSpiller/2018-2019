from bs4 import BeautifulSoup
import requests
import os
from playsound import playsound

def sanitizeString(str1):
    garbageChars = "\\'\",!?.[]:;%&*\n"
    for c in garbageChars:
        str1 = str1.replace(c, "")
    str1 = str1.lower()
    str1 = str1.strip()
    return str1

def GetPageSoup():
    page = requests.get("https://theportalwiki.com/wiki/GLaDOS_voice_lines")
    # print(page)
    return BeautifulSoup(page.content, 'html.parser')

def gen_getlitag():
    liTagList = GetPageSoup().find_all('i')
    for li in liTagList:
        yield li

def GetDownloadUrl(audioName):
    for item in gen_getlitag():
        curr_iTagText = sanitizeString(item.get_text())
        #print(curr_iTagText)
        if sanitizeString(audioName) == curr_iTagText:
            return (item.next_element.next_element.next_element.next_element.next_element).a['href']
        
    print("Could not find audio file:")
    print(f"looking for '{sanitizeString(audioName)}'")
    exit()

def DownloadAudio(link):
    # get file name
    # print(f"Link: {link}")
    fileName = link.split("/")[-1]
    print(f"Downloading file {fileName}")
    
    r = requests.get(link, stream = True)

    # start download
    with open("Audio\\" + fileName, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
    fileLoc = os.getcwd() + "\\Audio\\" + fileName
    # print(f"Downlaoded file {fileName} in location {fileLoc}")
    return fileLoc
    
def FinalPlaySound(quote):
    playsound(DownloadAudio(GetDownloadUrl(quote)))
    return
