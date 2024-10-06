import recordAudio
import chatAPI

words=[]
theme="Theme: Words relating to Animals. Word: "
while True:
    recordAudio.record(2,'output.wav')

    
    transcript=chatAPI.audioToText('output.wav')

    #chatAPI.textToAudio(transcript)
    if transcript not in words:
        words.append(transcript)
    
    else:
        print("PLAYER OUT")
        break

    transcript=theme+transcript
    output=chatAPI.prompt(transcript)
    if output == "False":
        print("PLAYER OUT")
        break
    print("Correct Next Player")
#chatAPI.textToAudio(output)
# '''