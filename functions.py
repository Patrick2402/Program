from generate_data import fourier, generate_sinus
import matplotlib.pyplot as plt
import numpy as np
from math import ceil, exp


def one_sinus():
    amplitude           = float(input("amplitude: "))
    freqency_one_signal = float(input("frequency [Hz]: "))
    start               = float(input("start time [s]: "))
    duration_time       = float(input("signal duration time [s]: "))
    phi                 = float(input("pahse: "))
    samplings_rate      = float(input("sampling rate: "))
    signal              = generate_sinus(   amplitude=amplitude, frequency=freqency_one_signal, start=start ,obt=duration_time, phi=phi, samplings_rate=samplings_rate)
    signal              = fourier(signal)

    draw_plot(  xdata=signal["timeline"], 
                    ydata=signal["data_about_signal"], 
                    title="sin(x)", 
                    xlabel="Time [s]", 
                    ylabel="Amplituda")

    draw_plot(  xdata=signal["frequency_fft"],
                    ydata=signal["fft"],
                    title="Plot in frequency domain",
                    xlabel="Frequency [Hz]",
                    ylabel="|signal(f)|")


def two_singals_merge(signal_one, signal_two):
    signal = {}
    signal["timeline"] = np.arange(
    signal_one["start"] * signal_one["samp_rate"],
    (signal_two["start"] + signal_two["ot"]) * signal_one["samp_rate"]
) / signal_one["samp_rate"] if signal_one["timeline"][-1] < signal_two["timeline"][-1] else np.arange(
    signal_two["start"] * signal_two["samp_rate"],
    (signal_one["start"] + signal_one["ot"]) * signal_two["samp_rate"]
) / signal_two["samp_rate"] if signal_one["timeline"][-1] > signal_two["timeline"][-1] else signal_one["timeline"]

    data_about_signal = []
    data_time_signal_one = dict(zip(signal_one["timeline"], signal_one["data_about_signal"]))
    data_time_signal_two = dict(zip(signal_two["timeline"], signal_two["data_about_signal"]))
    for time_probe in signal["timeline"]:
        if time_probe in signal_one["timeline"] and time_probe in signal_two["timeline"]:
            data_about_signal.append(data_time_signal_one[time_probe]+data_time_signal_two[time_probe])
        elif time_probe in signal_one["timeline"] and time_probe not in signal_two["timeline"]:
            data_about_signal.append(data_time_signal_one[time_probe])
        elif time_probe not in signal_one["timeline"] and time_probe in signal_two["timeline"]:
            data_about_signal.append(data_time_signal_two[time_probe])
        else:
            data_about_signal.append(0)

    signal["data_about_signal"] = data_about_signal
    signal["samp_rate"] = signal_one["samp_rate"]
    signal["ot"] = ceil(signal["timeline"][-1])
    signal["f"] = "{}, {}".format(signal_one["f"], signal_two["f"])
    return signal

# funkcja wyswietlania wykresow 

def draw_plot(xdata, ydata, title, xlabel, ylabel, xdata2=[]):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if len(xdata2) <= 0:
        plt.plot(xdata, ydata, color='g', label='Signal_sin')
    plt.legend(loc='upper left')
    plt.show()


#funckja zbierania oraz wyswietlania informacji/ danych dla etapu 1.2

def two_sinus():
    amplitude_one            = float(input("Amplitude of first signal: "))
    frequency_one           = float(input("Frequency of first signal [Hz]: "))
    start_time_one          = float(input("Start time of first signal [s]: "))
    duration_time_of_signal_one  = float(input("Signal one duration time [s]: "))
    phi_one            = float(input("Pahse of first signal: "))
    amplitude_two            = float(input("Amplitude of second signal: "))
    frequency_two           = float(input("Frequency of second signal [Hz]: "))
    start_time_two          = float(input("Start time of second signal[s]: "))
    duration_time_of_signal_two  = float(input("Signal two duration time [s]: "))
    phi_two            = float(input("Pahse of second signal: "))
    samplings_rate  = float(input("Sampling rate of both singals: "))
    signal_one      = generate_sinus(  amplitude=amplitude_one, frequency=frequency_one, start=start_time_one, obt=duration_time_of_signal_one, phi=phi_one, samplings_rate=samplings_rate)
    signal_two      = generate_sinus(  amplitude=amplitude_two, frequency=frequency_two, start=start_time_two, obt=duration_time_of_signal_two, phi=phi_two, samplings_rate=samplings_rate)
    signal          = two_singals_merge(signal_one, signal_two) # Suma sygnałów 
    signal          = fourier(signal) # generowanie wykresu transformaty fouriera
    draw_plot(  xdata=signal["timeline"], ydata=signal["data_about_signal"], title="Signal One", xlabel="Time [s]", ylabel="Amplituda")
    draw_plot(  xdata=signal["frequency_fft"], ydata=signal["fft"], title="", xlabel="Frequency [Hz]", ylabel="|signal(f)|" )




################
# Zadanie nr 2 #
################

def second_stage():
    A =             float(input("amplitude: "))
    K =             float(input("parameter K: "))
    n =             float(input("parameter n: "))
    t1 =            float(input("parameter t1 [s]: "))
    t2 =            float(input("parameter t2 [s]: "))
    start =    float(input("start time [s]: "))
    duration_time = float(input("signal duration time [s]: "))
    frequency =     float(input("frequency [Hz]: "))
    phi =           float(input("pahse: "))
    samplings_rate = float(input("sampling rate: "))
    signal = {}
    time_samples = samplings_rate*(duration_time+start)
    signal["timeline"] = np.arange(start*samplings_rate, time_samples)/samplings_rate
    signal["data_about_signal"] = [A * K * ((t/t1)**n)/(1+(t/t1)**n) * exp(-(t/t2)) * np.cos(2*np.pi*t*frequency+phi) for t in signal["timeline"]]
    signal["samp_rate"] = samplings_rate
    signal["f"] = frequency
    signal["ot"] = duration_time
    signal = fourier(signal)

    draw_plot(  xdata=signal["timeline"], ydata=signal["data_about_signal"], title="Time domain", xlabel="Time [s]", ylabel="Amplituda")
    draw_plot(  xdata=signal["frequency_fft"], ydata=signal["fft"], title="Frequency domain", xlabel="Frequency [Hz]", ylabel="|signal(f)|")

