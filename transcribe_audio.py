import speech_recognition as speechRec

from os import path

from pydub import AudioSegment

import json

import googleapiclient


#amr_file =  AudioSegment.from_file("file_1.amr", format="amr")

#amr_file.export("file_1_mp3.mp3", format="mp3")

api_key = "AIzaSyCbc287fEwoAK0XjFsQzCu_Ax5kIW9D5Q8"
with open('transcribe_Project-597c3c9acfc3.json') as f:
    data = json.load(f)
json_string = json.dumps(data)
file_to_transcribe = "file_1.wav"
#file_to_transcribe = "20200315_123641.wav"
recognizer = speechRec.Recognizer()

file = open("transcription.txt", "w")

#audio_file = recognizer.AudioFile(file_to_transcribe)

with speechRec.AudioFile(file_to_transcribe) as source:
    audio_data = recognizer.record(source)

    text = recognizer.recognize_google_cloud(audio_data, credentials_json=json_string, language="sv-SE")

    #print(text)
    file.write(text)
    file.close




