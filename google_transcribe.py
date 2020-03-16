from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io

audio_file = "file_1.wav"
def long_file_rec(storage_uri):

    client = speech_v1.SpeechClient()

    language_code = "sv-SE"

    sample_rate_hertz = 48000

    storage_uri = 'gs://interview_transcriptions/file_1.wav'

    transcript = ''

    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding":encoding,
        "audio_channel_count":2,
        "enable_automatic_punctuation": True,
        #"enable_speaker_diarization": True,
        #"diarization_speaker_count": 2,
    }

    #with io.open(audio_file, "rb") as f:
    #    content = f.read()
    #audio = {"content": content}

    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"waiting for operation to complete")
    response = operation.result()

    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript  
       # print(u"transcript: {}".format(alternative.transcript))


def main():
    import argparse

    parser = argparse.ArgumentParser()
    #parser.add_argument(
    #    "--local_file_path", type=str, default="file_1.wav"
    #)
    parser.add_argument(
        "--storage_uri", 
        type=str,
        default="gs://interview_transcriptions/file_1.wav"
    )
    args= parser.parse_args()
    #save_text = long_file_rec(args.local_file_path)
    save_text=long_file_rec(args.storage_uri)

    file = open("transcription_with_delimiters.txt", "w")
    for word in save_text:
        file.write(word)
        if "." in word:
            file.write("\n")
    file.close
 

if __name__ == "__main__":
    main()

