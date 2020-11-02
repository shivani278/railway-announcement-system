import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined +=AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3')
    #1 generate kripya dhyan de
    start=88000
    finish=90200
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    #2 
    #3 
    start=91000
    finish=92200
    audioProcessed=audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format="mp3")
    #4
    #5
    start=94000
    finish=95000
    audioProcessed=audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")
    #6
    #7
    start=96000
    finish=98900
    audioProcessed=audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")
    #8
    #9
    start=105500
    finish=108200
    audioProcessed=audio[start:finish]
    audioProcessed.export("10_hindi.mp3",format="mp3")

    #10
    #12
    start=109000
    finish=112250
    audioProcessed=audio[start:finish]
    audioProcessed.export("12_hindi.mp3",format="mp3")



def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        #2
        textToSpeech(item['from'],'2_hindi.mp3')
        #4
        textToSpeech(item['via'] ,'4_hindi.mp3')
        #6
        textToSpeech(item['to'],'6_hindi.mp3')
        #8
        textToSpeech(item['train_no'],'8_hindi.mp3')
        #9
        textToSpeech(item['train_name'],'9_hindi.mp3')

        #11
        textToSpeech(item['platform'],'11_hindi.mp3')

        
        audios=[f"{i}_hindi.mp3"for i in range(1,13)]
        announcement=mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format='mp3')
        
        
if __name__ == "__main__":
    print("generating skeleton")
    generateSkeleton()
    print("now generating announcement")
    generateAnnouncement("announce_hindi(1).xlsx")
    print('created audio in the folder..')



