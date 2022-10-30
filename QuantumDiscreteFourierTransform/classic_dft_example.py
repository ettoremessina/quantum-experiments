import numpy as np
import matplotlib.pyplot as plt

#signal generation

duration = 2. #in seconds
sampling_rate = 100. #per seconds
sampling_period = 1./sampling_rate
discrete_times = np.arange(0, duration, sampling_period)
num_of_samples = len(discrete_times)

frequency = 5. #in Hz
amplitude = 1.4 #in Volts, for example
phase = 0. #in radiant
sampled_values =  amplitude * np.sin(2 * np.pi * frequency * discrete_times + phase)

frequency = 10.
amplitude = 0.8
phase = np.pi / 2.
sampled_values += amplitude * np.sin(2 * np.pi * frequency * discrete_times + phase)

plt.plot(discrete_times, sampled_values, 'b')
plt.title('Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()


#Discrete Fourier Transform using SciPy
import scipy.fft as spf

transformed_signal = np.abs(spf.fft(sampled_values)[0:num_of_samples//2])
normalized_transformed = (2.0/num_of_samples) * transformed_signal
discrete_frequencies = spf.fftfreq(num_of_samples, sampling_period)[:num_of_samples//2]

plt.plot(discrete_frequencies, normalized_transformed, 'r')
plt.title('DFT by SciPy fft')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()
plt.show()



#Discrete Fourier Matrix Transform

def DFTByMatrix(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    fourier_matrix = np.exp(-2j * np.pi * k * n / N)
    transf_signal = np.dot(fourier_matrix, signal)
    return transf_signal

transformed_signal = np.abs(DFTByMatrix(sampled_values))[0:num_of_samples//2]
normalized_transformed = (2.0/num_of_samples) * transformed_signal
discrete_frequencies = (discrete_times / sampling_period)[:num_of_samples//2]

plt.plot(discrete_frequencies, normalized_transformed, 'g')
plt.title('DFT by Matrix')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()
plt.show()

