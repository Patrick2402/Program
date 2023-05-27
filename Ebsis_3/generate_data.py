import numpy as np
import matplotlib.pyplot as plt
from math import ceil, exp

# prosta funkcja do generowania damnych do wykresu sinusoidalnego.

def generate_sinus(amplitude, frequency, obt, phi, samplings_rate, start):
    time_samples = samplings_rate*(obt+start)
    timeline = np.arange(start*samplings_rate, time_samples)/samplings_rate
    signal = amplitude*np.sin(2*np.pi*frequency*timeline+phi)
    return {"timeline": timeline, "data_about_signal": signal, "A": amplitude, "f": frequency, "ot": obt, "phi": phi, "samp_rate": samplings_rate, "start": start}  



# Funkcja pozwalająca obliczyc dane do pozniejszego wygenerowania wykresu widma sygnalu 

def fourier(signal):
    signal["frequency_fft"] = np.fft.fftfreq(len(signal["timeline"]), 1/signal["samp_rate"])[:len(signal["timeline"])//2]
    signal["fft"] = np.absolute(np.fft.fft(signal["data_about_signal"]))[:len(signal["timeline"])//2] 
    return signal