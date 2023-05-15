import numpy as np
import matplotlib.pyplot as plt

def display_sin(amplituda, czestotliwosc, phi):
    czas = np.linspace(0, 2*np.pi, 1000)  # Przedział czasu od 0 do 2π
    wartosci = amplituda * np.sin(czestotliwosc * czas + phi)  # Obliczanie wartości sinusa

    # Rysowanie wykresu
    plt.plot(czas, wartosci)
    plt.xlabel('Czas')
    plt.ylabel('Wartość sinusa')
    plt.title('Wykres sinusa')
    plt.grid(True)
    plt.show()

# Przykładowe wywołanie funkcji
amplituda = 1.5
czestotliwosc = 2
phi = np.pi/2
display_sin(amplituda, czestotliwosc, fazowka)
