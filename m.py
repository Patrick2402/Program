import numpy as np
import matplotlib.pyplot as plt
from math import ceil, exp
import argparse


# def rysuj_sumowane_sinusy(amplituda1, f1, phi1, amplituda2, f2, phi2 ):

#     czas = np.arange(0, np.pi*2, 0.05)
#     sinus1 = amplituda1 * np.sin(float(f1) * czas + float(phi1))  # Obliczanie wartości pierwszego sinusa
#     sinus2 = amplituda2 * np.sin(float(f2) * czas + float(phi2))  # Obliczanie wartości drugiego sinusa
#     suma = sinus1 + sinus2  # Sumowanie sinusoid


#     plt.subplot(2, 2, 1)
#     plt.plot(czas, sinus1, color = 'r')
#     plt.plot(czas, sinus2, color = 'b')
#     plt.xlabel('Czas')
#     plt.ylabel('Wartość sinusa')
#     plt.title('Sinusy ')
#     plt.grid(True)

#     plt.subplot(2, 2, 3)
#     plt.plot(czas, suma)
#     plt.xlabel('Czas')
#     plt.ylabel('Wartość sinusa')
#     plt.title('Suma dwóch sinusoid')
#     plt.grid(True)

#     # Obliczanie transformaty Fouriera dla sumy sinusoid
#     transformata = np.fft.fft(suma)
#     czestotliwosci = np.fft.fftfreq(len(suma), d=1/(2*np.pi))

#     # Rysowanie wykresu transformaty Fouriera dla sumy sinusoid
#     plt.subplot(2, 2, 4)
#     plt.plot(czestotliwosci, np.abs(transformata))
#     plt.xlabel('Częstotliwość')
#     plt.ylabel('Amplituda')
#     plt.title('Transformaty Fouriera dla sumy sinusoid')
#     plt.grid(True)


#     plt.tight_layout()
#     plt.show()

# # Przykładowe wywołanie funkcji
# amplituda1 = 1.5
# czestotliwosc1 = 2
# fazowka1 = np.pi/2

# amplituda2 = 0.8
# czestotliwosc2 = 3
# fazowka2 = np.pi

def one():

    amplituda1 = float((input("Amplituda 1: ")))
    f1 = float(input("Czestotliwosc 1: "))
    phi1 = float(input("Faza 1: "))
    start = float(input("Start: "))
    duration = float(input("Duration: "))
    probkowanie = float(input("Probkowanie: "))

    #czas = np.arange(0, np.pi*2, 0.05)

    probki_czasu = probkowanie*(duration+start)
    czas = np.arange(start*probkowanie,probki_czasu)/probkowanie

    sinus1 = amplituda1 * np.sin(float(f1) * czas + float(phi1))  # Obliczanie wartości pierwszego sinusa
    plt.subplot(2,1,1)
    plt.plot(czas, sinus1, color = 'r')
    plt.xlabel('Czas')
    plt.ylabel('Wartość sinusa')
    plt.title('Pojedynczy Sinus ')
    plt.grid(True)

    plt.subplot(2,1,2)
    #transformata = np.fft.fft(sinus1)
    transformata = np.absolute(np.fft.fft(sinus1))[:len(czas)//2] 
    czestotliwosci = np.fft.fftfreq(len(sinus1), d=1/(2*np.pi))
    czestotliwosci = np.fft.fftfreq(len(sinus1), 1/100)[:len(czas)//2]

    plt.plot(czestotliwosci, np.abs(transformata))
    plt.xlabel('Częstotliwość')
    plt.ylabel('Amplituda')
    plt.title('Transformaty Fouriera dla sumy sinusoid')
    plt.grid(True)
    plt.tight_layout()
    plt.show()




# amplituda1 = int(input("Amplituda 1: "))
# f1 = input("Czestotliwosc 1: ")
# phi1 = input("Faza 1: ")


# amplituda2 = int(input("Amplituda 2: "))
# f2 = input("Czestotliwosc 2: ")
# phi2 = input("Faza 2: ")

#rysuj_sumowane_sinusy(amplituda1, f1, phi1, amplituda2, f2, phi2)


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-one', '--part1_one',  action="store_true",  help='One signal in part 1')
parser.add_argument('-sum', '--part1_two',  action="store_true",  help='Two signals in part 1')
parser.add_argument('-two'   , '--part2',      action="store_true",  help='One signal in part 2')
args = parser.parse_args()

if args.part1_one:
    one()
elif args.part1_two:
    pass 
elif args.part2:
    pass