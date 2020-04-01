from gtts import gTTS
import speech_recognition as sr
from pyaudio import PyAudio
import sys
import os
import random
import time as t
command = []
_isHello = []


print('ai start!')

def workDobby():
    print('dobby is working!!')
    os.sys("afplay /Users/choihyomin/Desktop/raspbianpiDobby/soundeffect/Wood_Plank_Flicks.mp3")

    while True:
        r = sr.Recognizer()
        _isWorking = False
        with sr.Microphone() as source:
            audio = r.listen(source, timeout = 1)
        try:
            text = r.recognize_google(audio)
            print(text)
            if 'stop' in text or 'Stop' in text:
                break;
            
        except:
            print('call me later...')
            break

def turnoff():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        print("you : ",text)
        if(text == 'Stop' or text == 'stop'):
            _isWorking = True
            
            print("Dobby : hello master")
            workDobby()
    except:
        print('oh my god!')

def turnmusic():
    print('turn music on')
    whichmusic = random.randint(1,1)
    msic = str(whichmusic) + '.mp3'
    if(whichmusic == 1):
        print('this is nice rock music')
    os.system("afplay /Users/choihyomin/Desktop/raspbianpiDobby/music/Infiltration_Device.mp3")


def reaction():
    speaks = ["oh really?","that's great","awesome!","ah-ha","hmmm"]
    _sLen = len(speaks)
    pick = str(random.randint(1,_sLen)) + ".mp3"
    os.system("afplay 경로/"+pick)
'''
blink = "blink"
blink.save('blink.mp3')
turnmusic = "Dobby will turn music on"     gtts에서 문장만 따로 저장하는 방법 검색하기
turnmusic.save('turnmusicon.mp3')
'''
#always steady
while True:
    r = sr.Recognizer()
    _isWorking = False
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        print("you : ",text)
        if(text == 'Hello' or text == 'hello'):
            _isWorking = True
            
            print("Dobby : hello master")
            workDobby()
    except:
        print('oh my god!')
    
    if(len(command) > 0):
        if 'Music' in command or 'music' in command:
            turnmusic()
            command.clear()
        