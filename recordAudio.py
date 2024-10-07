import wave
import sys
import pyaudio


#record audio of seconds length and the output file name
def record(seconds,output):
    #audio format chunk and channel 
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 44100
    RECORD_SECONDS = seconds
    #open file and start recording
    with wave.open(output, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        #write to output file the recording each time
        for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            wf.writeframes(stream.read(CHUNK))
        print('Done')

        stream.close()
        p.terminate()
#unused for now but used to open and play audio files
class AudioFile:
    chunk = 1024

    def __init__(self, file):
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()
