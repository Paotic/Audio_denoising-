import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import wave as we


def read_wav(wavfile):
    f = wavfile
    params = f.getparams() #Gets the parameters of the wav file

    nchannels, sampwidth, framerate, nframes = params[:4] #Extracts the number of channels, sample width, frame rate and number of frames from the params tuple and assigns them to separate variables
    strData = f.readframes(nframes) #Reads the wave data from the wave file
    waveData = np.frombuffer(strData, dtype=np.int16) #Converts the byte string strData

    time = np.arange(0, nframes)*(1.0 / framerate) #Creates an array represents the time axis of the wave data
    plt.plot(time, waveData)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Wavedata")
    plt.show()
    return (waveData, time)


print("\nInput test_noise wave data:")
f = we.open("test_noise.wav", 'rb')

data, time = read_wav(f)

def fft_wav(waveData):
    f_array = np.fft.fft(waveData) #Computes the FFT of the waveData
    f_abs = f_array
    axis_f = np.linspace(0, 100, int(len(f_array))) #Creates an array represents the frequency axis of the FFT data


    plt.plot(axis_f, np.abs(f_abs[0:len(axis_f)]))
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude spectrum")
    plt.title("Tile map")
    plt.show()
    return f_abs

wave_fft = fft_wav(data)

step_hz = 100/(len(data)/2) #Computes the step size in Hertz
tab_hz = 68 # stop-band frequency value
new_wav = wave_fft.copy()

for i in range(int(tab_hz/step_hz), (len(wave_fft) - int(tab_hz/step_hz))):
    new_wav[i]=0  
    #Loops through the frequency bins of the new_wav array, excluding the bins in the stop-band, and sets their values to zero. 
    #This effectively removes the frequencies in the stop-band from the spectrum
axis_f = np.linspace(0, 100, int(len(wave_fft)))
plt.plot(axis_f, np.abs(new_wav[0:len(axis_f)]))

plt.xlabel("Frequency")
plt.ylabel("Amplitude spectrum")
plt.title("Tile map after wave filtering")
plt.show()

filtered_wave = np.fft.ifft(new_wav)

# Plotting original and filtered signals
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, data)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Original Signal")

plt.subplot(2, 1, 2)
plt.plot(time, filtered_wave.real)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered Signal")

plt.tight_layout()
plt.show()

save_wav = filtered_wave.real.reshape((len(filtered_wave), 1)).T.astype(np.short)
f = we.open("freq_flitering.wav", "wb")

f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(16000)
f.writeframes(save_wav.tobytes())
f.close()
