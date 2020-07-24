import os
import numpy as np
import wave


# wav转为pcm
def wav2pcm(filename):
    f = open(filename + ".wav", 'rb')
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=np.int16)
    pcm_filename = filename + ".pcm"
    data.tofile(pcm_filename)
    f.close()
    return pcm_filename


def pcm2wav(filename):
    f = open(filename + ".pcm", 'rb')
    str_data = f.read()
    wave_out = wave.open(filename + "_new.wav", 'wb')
    wave_out.setnchannels(1)
    wave_out.setsampwidth(2)
    wave_out.setframerate(44100)
    wave_out.writeframes(str_data)

if __name__ == "__main__":
    wav2pcm("../test")
    pcm2wav("../test")