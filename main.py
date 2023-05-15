import numpy as np
import matplotlib.pyplot as plt
from math import ceil, exp
import argparse

def generate_sinusoidal_signal(amplitude=1, frequency=1, observation_time=1, phi=0, sampling_rate=500, start_time=0):
    time_samples = sampling_rate*(observation_time+start_time)
    timeline = np.arange(start_time*sampling_rate, time_samples)/sampling_rate
    sig = amplitude*np.sin(2*np.pi*frequency*timeline+phi)

    return {"timeline": timeline, "data": sig, "A": amplitude, "f": frequency, "ot": observation_time, "phi": phi, "samp_rate": sampling_rate, "start_time": start_time}    

def generate_fft(sig):
    sig["fft_freq"] = np.fft.fftfreq(len(sig["timeline"]), 1/sig["samp_rate"])[:len(sig["timeline"])//2]
    sig["fft"] = np.absolute(np.fft.fft(sig["data"]))[:len(sig["timeline"])//2] 
    return sig

def merge_signals(sig1, sig2):
    sig = {}
    if sig1["timeline"][-1] < sig2["timeline"][-1]:
        sig["timeline"] = np.arange(sig1["start_time"]*sig1["samp_rate"], (sig2["start_time"]+sig2["ot"])*sig1["samp_rate"])/sig1["samp_rate"]
    elif sig1["timeline"][-1] > sig2["timeline"][-1]:
        sig["timeline"] = np.arange(sig2["start_time"]*sig2["samp_rate"], (sig1["start_time"]+sig1["ot"])*sig2["samp_rate"])/sig2["samp_rate"]
    else:
        sig["timeline"] = sig1["timeline"]

    data = []
    sig1_time_data = dict(zip(sig1["timeline"], sig1["data"]))
    sig2_time_data = dict(zip(sig2["timeline"], sig2["data"]))
    for time_probe in sig["timeline"]:
        if time_probe in sig1["timeline"] and time_probe in sig2["timeline"]:
            data.append(sig1_time_data[time_probe]+sig2_time_data[time_probe])
        elif time_probe in sig1["timeline"] and time_probe not in sig2["timeline"]:
            data.append(sig1_time_data[time_probe])
        elif time_probe not in sig1["timeline"] and time_probe in sig2["timeline"]:
            data.append(sig2_time_data[time_probe])
        else:
            data.append(0)

    sig["data"] = data
    sig["samp_rate"] = sig1["samp_rate"]
    sig["ot"] = ceil(sig["timeline"][-1])
    sig["f"] = "{}, {}".format(sig1["f"], sig2["f"])
    return sig

def generate_plot(xdata, ydata, title, xlabel, ylabel, xdata2=[], ydata2=[]):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if len(xdata2) > 0:
        plt.plot(xdata2, ydata2, color='b', label='Referencyjny')
        plt.plot(xdata, ydata, color='r', label='Zmodyfikowany')
    else:
        plt.plot(xdata, ydata, color='g', label='Sygnal')
    plt.legend(loc='upper left')
    plt.show()

def display_info(info):
    print("\n"+str(info))
    print("-"*len(info))

def stage1_one_signal():
    display_info("Enter parameters of the signal")
    amplitude           = float(input("Enter amplitude: "))
    freq                = float(input("Enter frequency [Hz]: "))
    start_time          = float(input("Enter start time [s]: "))
    duration_time       = float(input("Enter signal duration time [s]: "))
    phi                 = float(input("Enter pahse: "))
    sampling_rate       = float(input("Enter sampling rate: "))

    sig = generate_sinusoidal_signal(   amplitude=amplitude,
                                        frequency=freq,
                                        start_time=start_time,
                                        observation_time=duration_time,
                                        phi=phi,
                                        sampling_rate=sampling_rate)
    sig = generate_fft(sig)

    print("[i] Close the plot window to see antoher")
    generate_plot(  xdata=sig["timeline"], 
                    ydata=sig["data"], 
                    title="First Chart", 
                    xlabel="Czas [s]", 
                    ylabel="Amplituda")

    generate_plot(  xdata=sig["fft_freq"],
                    ydata=sig["fft"],
                    title="",
                    xlabel="Czestotliwosc [Hz]",
                    ylabel="|sig(f)|")


def stage1_two_signals():
    display_info("Enter parameters of the first signal")
    amp1 =              float(input("Enter amplitude: "))
    freq1 =             float(input("Enter frequency [Hz]: "))
    start_time1 =       float(input("Enter start time [s]: "))
    duration_time1 =    float(input("Enter signal duration time [s]: "))
    phi1 =              float(input("Enter pahse: "))
    
    display_info("Enter parameters of the second signal")
    amp2 =              float(input("Enter amplitude: "))
    freq2 =             float(input("Enter frequency [Hz]: "))
    start_time2 =       float(input("Enter start time [s]: "))
    duration_time2 =    float(input("Enter signal duration time [s]: "))
    phi2 =              float(input("Enter pahse: "))
    
    display_info("Enter sampling rate")
    sampling_rate = float(input("Enter sampling rate: "))

    sig1 = generate_sinusoidal_signal(  amplitude=amp1,
                                        frequency=freq1,
                                        start_time=start_time1,
                                        observation_time=duration_time1,
                                        phi=phi1,
                                        sampling_rate=sampling_rate)
    
    sig2 = generate_sinusoidal_signal(  amplitude=amp2,
                                        frequency=freq2,
                                        start_time=start_time2,
                                        observation_time=duration_time2,
                                        phi=phi2,
                                        sampling_rate=sampling_rate)

    sig = merge_signals(sig1, sig2)
    sig = generate_fft(sig)
    
    print("[i] Close the plot window to see antoher")
    generate_plot(  xdata=sig["timeline"], 
                    ydata=sig["data"], 
                    title="", 
                    xlabel="Czas [s]", 
                    ylabel="Amplituda")

    generate_plot(  xdata=sig["fft_freq"],
                    ydata=sig["fft"],
                    title="",
                    xlabel="Czestotliwosc [Hz]",
                    ylabel="|sig(f)|" )

def stage2():
    display_info("Enter parameters of the signal")
    A =             float(input("Enter amplitude: "))
    K =             float(input("Enter parameter K: "))
    n =             float(input("Enter parameter n: "))
    t1 =            float(input("Enter parameter t1 [s]: "))
    t2 =            float(input("Enter parameter t2 [s]: "))
    start_time =    float(input("Enter start time [s]: "))
    duration_time = float(input("Enter signal duration time [s]: "))
    frequency =     float(input("Enter frequency [Hz]: "))
    phi =           float(input("Enter pahse: "))
    sampling_rate = float(input("Enter sampling rate: "))

    sig = {}
    time_samples = sampling_rate*(duration_time+start_time)
    sig["timeline"] = np.arange(start_time*sampling_rate, time_samples)/sampling_rate
    sig["data"] = [A * K * ((t/t1)**n)/(1+(t/t1)**n) * exp(-(t/t2)) * np.cos(2*np.pi*t*frequency+phi) for t in sig["timeline"]]
    sig["samp_rate"] = sampling_rate
    sig["f"] = frequency
    sig["ot"] = duration_time
    sig = generate_fft(sig)

    print("[i] Close the plot window to see antoher")
    generate_plot(  xdata=sig["timeline"], 
                    ydata=sig["data"], 
                    title="", 
                    xlabel="Czas [s]", 
                    ylabel="Amplituda")

    generate_plot(  xdata=sig["fft_freq"],
                    ydata=sig["fft"],
                    title="",
                    xlabel="Czestotliwosc [Hz]",
                    ylabel="|sig(f)|")


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p1one', '--part1_one',  action="store_true",  help='One signal in part 1')
parser.add_argument('-p1two', '--part1_two',  action="store_true",  help='Two signals in part 1')
parser.add_argument('-p2'   , '--part2',      action="store_true",  help='One signal in part 2')
args = parser.parse_args()

if args.part1_one:
    stage1_one_signal()
elif args.part1_two:
    stage1_two_signals()
elif args.part2:
    stage2()