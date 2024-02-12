import audioTest
import chatAPI

audioTest.record(12,'output.wav')


transcript=chatAPI.audioToText('output.wav')


chatAPI.textToAudio(transcript)
