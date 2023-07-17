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
data, time = read_wav(f) #assigns the resulting sample data array and time array to the variables data and time, respectively.
length=data.shape[0]/16000 #Computes the duration of the audio signal in seconds by dividing the number of samples in the data array


time = np.linspace(0., length, data.shape[0])


def moving_avg(audio_data,avg_length):
    new_data=[]
    for i in range(data.shape[0]-avg_length+1):
        new_data.append(np.average(data[i:i+avg_length])) #computes the average of the current avg_length samples of the input data
    new_data=np.array(new_data).reshape((-1,1)) #Converts the new_data list to a numpy, reshapes it into a 2D array
    new_data=np.int32(new_data) #Converts the resulting 2D array to a 32-bit integer type
    return new_data    

for i in range(1,11):
    new_data=moving_avg(data,i)
    time = np.linspace(0., length, new_data.shape[0]) #Computes the time array corresponding to new_data
    save_wav = new_data.real.reshape((len(new_data), 1)).T.astype(np.short) #Reshapes new_data into a 2D array with a single column, converts it to a 16-bit short integer type 
    f = we.open("moving_avg_fliter.wav", "wb")
    f.setnchannels(1) #Sets the number of audio channels in the wave file to 1
    f.setsampwidth(2) #Sets the sample width to 2
    f.setframerate(16000) #Sets the frame rate to 16000
    f.writeframes(save_wav.tostring()) #Writes the filtered audio data to the wave file
    f.close()

f = we.open("moving_avg_fliter.wav", 'rb')
print("\nTime domain(moving average) Filter wavedata:")
read_wav(f)

