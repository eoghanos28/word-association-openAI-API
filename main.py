import recordAudio
import chatAPI

words=[]
#Set the theme and instructions for gpt-4-turbo-preview
theme="Theme: Words relating to Animals. Word: "
while True:
    #Record 2 seconds of audio (plays saying their answer)
    recordAudio.record(2,'output.wav')

    #feed to chatAPI function and return string
    transcript=chatAPI.audioToText('output.wav')

    #Add it to used words 
    if transcript not in words:
        words.append(transcript)
    #If word used then player is out
    else:
        print("PLAYER OUT")
        break
    #Check to see if word relates to the theme
    transcript=theme+transcript
    output=chatAPI.prompt(transcript)
    #If not related player is out otherwise next player
    if output == "False":
        print("PLAYER OUT")
        break
    print("Correct Next Player")
