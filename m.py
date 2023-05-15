import numpy as np
import matplotlib.pyplot as plt

def rysuj_wykres_sin(amplituda, czestotliwosc, fazowka):
    czas = np.linspace(0, 2*np.pi, 1000)  # Przedział czasu od 0 do 2π
    wartosci = amplituda * np.sin(czestotliwosc * czas + fazowka)  # Obliczanie wartości sinusa

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
fazowka = np.pi/2
rysuj_wykres_sin(amplituda, czestotliwosc, fazowka)
