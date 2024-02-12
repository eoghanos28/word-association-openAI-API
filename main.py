import audioTest
import chatAPI

audioTest.record(5,'output.wav')


transcript=chatAPI.audioToText('output.wav')

output=chatAPI.prompt(transcript)

chatAPI.textToAudio(output)
