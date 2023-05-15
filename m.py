import numpy as np
import matplotlib.pyplot as plt

def rysuj_sumowane_sinusy(amplituda1, czestotliwosc1, fazowka1, amplituda2, czestotliwosc2, fazowka2):
    czas = np.linspace(0, 2*np.pi, 1000)  # Przedział czasu od 0 do 2π
    sinus1 = amplituda1 * np.sin(czestotliwosc1 * czas + fazowka1)  # Obliczanie wartości pierwszego sinusa
    sinus2 = amplituda2 * np.sin(czestotliwosc2 * czas + fazowka2)  # Obliczanie wartości drugiego sinusa
    suma = sinus1 + sinus2  # Sumowanie sinusoid

    # Rysowanie wykresu sumy sinusoid
    plt.subplot(3, 1, 1)
    plt.plot(czas, sinus1, label='Sinus 1')
    plt.plot(czas, sinus2, label='Sinus 2')
    plt.plot(czas, suma, label='Suma')
    plt.xlabel('Czas')
    plt.ylabel('Wartość sinusa')
    plt.title('Sumowanie dwóch sinusoid')
    plt.grid(True)
    plt.legend()

    # Obliczanie transformaty Fouriera
    transformata = np.fft.fft(suma)
    czestotliwosci = np.fft.fftfreq(len(suma), d=1/(2*np.pi))

    # Rysowanie wykresu transformaty Fouriera
    plt.subplot(3, 1, 2)
    plt.plot(czestotliwosci, np.abs(transformata))
    plt.xlabel('Częstotliwość')
    plt.ylabel('Amplituda')
    plt.title('Transformaty Fouriera')
    plt.grid(True)

    # Rysowanie wykresu fazowego
    plt.subplot(3, 1, 3)
    plt.plot(czas, np.angle(transformata))
    plt.xlabel('Czas')
    plt.ylabel('Faza')
    plt.title('Wykres fazowy')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Przykładowe wywołanie funkcji
amplituda1 = 1.5
czestotliwosc1 = 2
fazowka1 = np.pi/2

amplituda2 = 0.8
czestotliwosc2 = 3
fazowka2 = np.pi

rysuj_sumowane_sinusy(amplituda1, czestotliwosc1, fazowka1, amplituda2, czestotliwosc2, fazowka2)
