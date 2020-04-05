from gtts import gTTS
import speech_recognition as sr
from pyaudio import PyAudio
import sys
import os
import random
import requests
import time as t
import playsound as PlaySound
#플레이사운드랑 os로 음악 재생하는거랑 무슨 차이일까??? 약간 플레이사운드는 고유의 플레이어모듈인가?
#os로 재생하면 그 운영체제의 기본 사운드 재생기가 필요한걸까??? 
#-------------------------------------------------------------------------------------------------------
command = []
_isHello = []
print('AI START!')

depress = [
    'creep.mp3',
    'fix-you.mp3',
    'scientist.mp3'
]

playful = [
    'up.mp3',
    'up-up.mp3',
    'A-Sky-Full-Of-Stars.mp3',
    'Viva-La-Vida.mp3'
]

energetic = [
    'born-for-this.mp3',
    'stronger.mp3',
    'centuries.mp3'
]


#-------------------------------------------------------------------------------------------------------
def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout = 2)
    try:
        text = r.recognize_google(audio,language='ko-KR')
        print('you : ',text)
        
        text = text.split()
        for text in text:
            command.append(text)
    except:
        print('다시 말해주시겠어요?')
#-------------------------------------------------------------------------------------------------------
def workDobby():
    print('dobby is working!!')
    os.system("afplay /Users/choihyomin/Desktop/raspbianpiDobby/soundeffect/Wood_Plank_Flicks.mp3")

    while True:
        print("working..")
        getAudio()
        if '그만' in command:
            break
        if '울고싶어' in command or '슬퍼' in command:
            command.clear()
            cheer()
        if '타이머' in command or '알람' in command:
            ts = gTTS('얼마나 설정할까요 주인님?',lang= 'ko')
            ts.save('ts.mp3')
            os.system("afplay ts.mp3")
            command.clear()
            Timer()

        if '대화' in command or '얘기' in command:
            command.clear()
            cheerconverstation()
            
        if '날씨' in command:
            command.clear()
            whatsWeather()

        if 'music' in command or 'Music' in command:
            command.clear()
            turnmusic()

        if '우울해' in command or '울적해' in command:
            command.clear()
            depressed()
        
        if '신나는' in command or '신나' in command:
            command.clear()
            play()

        if '운동' in command or '기똥찬' in command:
            command.clear()
            energy()

#-------------------------------------------------------------------------------------------------------
def depressed():
    dm = gTTS('도비가 주인님의 기분을 위로해드릴게요',lang = 'ko')
    dm.save('dm.mp3')
    os.system("afplay dm.mp3")
    r_Song = int(random.randint(0,2))
    print(depress[r_Song])
    tget = depress[r_Song]
    os.system('afplay '+ tget)
#-------------------------------------------------------------------------------------------------------
def play():
    pm = gTTS('오우! 오우! 북북치기 박치기 디제이 드랍 더 비트 뚜쒸뚜쒸!!',lang = 'ko') #신나는,#신나
    pm.save('pm.mp3')
    os.system("afplay pm.mp3")
    r_Song = int(random.randint(0,2))
    print(playful[r_Song])
    tget = playful[r_Song]
    os.system('afplay '+ tget)
#-------------------------------------------------------------------------------------------------------
def energy():
    em = gTTS('도비가 주인님만을 위한 기똥찬 에너제틱한 노래를 틀어드릴게요~! 오오우우우우우 예에에에에에에 ',lang = 'ko') # 운동, 기똥찬
    em.save('em.mp3')
    os.system("afplay em.mp3")
    r_Song = int(random.randint(0,2))
    print(energetic[r_Song])
    tget = energetic[r_Song]
    os.system('afplay '+ tget)
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
def cheer():
    #cm = gTTS('걱정마세요 주인님 도비가 기분좋게 해드릴게요',lang = 'ko')
    #cm.save('cm.mp3')
    os.system("afplay cm.mp3")
    #cs = gTTS('도비가 주인님의 기분을 위로해줄 노래를 들려드릴게요', lang = 'ko')
    #cs.save('cs.mp3')
    os.system('afplay cs.mp3')

    song_list = [
        '걱정말아요_그대.mp3',
        'Billie_Eilish-everything_i_wanted.mp3',
        'Everythings_Alright.mp3'
    ]
    r_Song = int(random.randint(0,2))
    print(song_list[r_Song])

    tget = song_list[r_Song]

    os.system('afplay '+ tget)
    

#-------------------------------------------------------------------------------------------------------
def cheerconverstation():
    print('도비가 왔어요')
    while True:
        react = [
            '힘내세요',
            '네에..',
            '그렇군요...',
            '그런일도 있는 법이죠 힘내세요',
            '제가 어떻게 감히 주인님을 이해할수있을까요?',
            '마음편히 우셔도 좋아요',
            '걱정말아요'
        ]
        pick = random.randint(0,len(react))
        cv = gTTS(react[pick],lang='ko')
        cv.save('cv.mp3')

        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, timeout = 2)
        try:
            text = r.recognize_google(audio,language='ko-KR')
            print(text)
            if text == '그만':
                break
            os.system('afplay cv.mp3')
                
        except:
            print('옆에서 계속 듣고있어요 ㅎㅎ 편히 말씀하세요')

   
#-------------------------------------------------------------------------------------------------------
def Timer():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout = 3)
    try:
        text = r.recognize_google(audio,language='ko-KR')
        print(text)
            
            
    except:
        print('call me later...')
#-------------------------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------------------------
def turnmusic():
    #tmo = gTTS('도비가 음악을 틀어드릴게요',lang='ko')
    #tmo.save('tmo.mp3')
    os.system("afplay tmo.mp3")

    whichmusic = random.randint(1,1)
    msic = str(whichmusic) + '.mp3'
    if(whichmusic == 1):
        print('this is nice rock music')
    os.system("afplay /Users/choihyomin/Desktop/raspbianpiDobby/music/Infiltration_Device.mp3")
    while True:
        print('waiting....')
        r = sr.Recognizer()
    
        with sr.Microphone() as source:
            audio = r.listen(source)
            
        try:
            text = r.recognize_google(audio)
            print("you : ",text)
            if(text == '그만'):
                #stp = gTTS('안녕히계세요 주인님 도비는 이만 물러갑니다',lang= 'ko')
                #stp.save('stp.mp3')
                os.system('afplay stp.mp3')
                sys.exit()
                break;
        except:
            print('((')
            print('))')

#------------------------------------------------------------------------------------------------
def reaction():
    speaks = ["정말요?","엄청나네요","멋져요","아하","으흠"]
    _sLen = len(speaks)
    pick = str(random.randint(1,_sLen)) + ".mp3"
    os.system("afplay 경로/"+pick)
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
def whatsWeather():
    url = 'https://api.openweathermap.org/data/2.5/weather?appid=cff1e8384fede827e297659a514f9141&q=Seoul'
    json_data = requests.get(url).json()
    weather = gTTS(json_data['weather'][0]['main'])
    weather.save('wdata.mp3')
    os.system('afplay wdata.mp3')


#-----------------------------------------------------------------------------------------------
#always steady
while True:
    print('처음으로 돌아갑니다!')
    r = sr.Recognizer()
    _isWorking = False
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio,language='ko-KR')
        print("you : ",text)
        if '도비야' in text:
            
            print("도비 : 부르셨어요?")
            #hm = gTTS('부르셨어요?',lang= 'ko')
            #hm.save('hm.mp3')
            os.system("afplay hm.mp3")
            workDobby()

        


    except:
        print('도비가 대기중이에요!')
    

        