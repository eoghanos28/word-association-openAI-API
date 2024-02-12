import audioTest
import chatAPI

words=[]
theme="Theme: Words relating to Zoos. Word: "
while True:
    audioTest.record(2,'output.wav')

    
    transcript=chatAPI.audioToText('output.wav')
    if transcript not in words:
        words.append(transcript)

    transcript=theme+transcript
    output=chatAPI.prompt(transcript)
    print(transcript)
    print(output)
    print(words)
#chatAPI.textToAudio(output)
