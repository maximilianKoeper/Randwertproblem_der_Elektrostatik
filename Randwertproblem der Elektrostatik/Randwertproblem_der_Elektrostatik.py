# 1. Computerübung zur Experimentalphysik 2 (SoSe 2019)
# Randwertproblem der Elektrostatik
# Maximilian Köper / Erik Steinkamp

# Module importieren

import Iterative as it
import Plot as plt

# Bibliotheken importieren

from numpy.random import randint
import numpy as np

print("Randwertproblem der Elektrostatik\nVersion 1.4\n")

# Initialisiere Array für Box
# Größe 50x50 
# Innere Größe 100x100
# Werte werden als float per numpy generiert 
# Zufallswerte sind zwischen 1 und 99

x = np.linspace(-10,40, num=102)
y = np.linspace(-25,25, num=102)

X, Y = np.meshgrid(x,y, sparse=True ,copy=True)
Z = np.zeros((102,102), dtype=np.float)

Z_x, Z_y = Z.shape

for i in range(Z_x):
   for j in range(Z_y):
       Z[i,j] = float(randint(1, high=99, size=None))


print("[*] Array initialisiert \n")

# Initialisiere Äußeren Leiter
# jeweils 1 Block oben und seitlich
# Potential außen = 0*100000V
# Innere Anordung wird nach User Eingabe initialisiert

i = 0
B = []
for i in range(Z_x):
    B.insert(i, 0)

Z[0] = B
Z[(Z_y-1)] = B

i = 0
for i in range(Z_x):
    Z[i][0] = 0
    Z[i][(Z_x-1)] = 0

print("[*] Äußerer Leiter initialisiert\n")

# User Abfrage 
# Welche Szenario soll berechnet werden
# A/B/C vgl. Aufgabenblatt

abc = input("Welche Anordnung soll berechnet werden (A/B/C): ")

# Generiert geladene Fläche (4x4)
# Diese Fläche ist bei allen Szenarios gleich

i = 46
j = 18
while i < 54:
    while j < 26:
        Z[i][j]=100
        j +=1
    j = 18
    i += 1

# Szenario wird generiert
# Szenario A muss nicht weiter verändert werden

if abc == "B":
    i = 10
    while i < 90:
        Z[i][51] = 0
        i += 1
elif abc == "C":
    i = 46
    j = 76
    while i < 54:
        while j < 84:
            Z[i][j]=-100
            j +=1
        j = 76
        i += 1
elif abc != "A":
    print("\n[*] Default: A")


# Fehler Schwellwert abfragen (DEFAULT: 0.1)
try:
    error_threshold = float(input("\nFehler Schwellwert eingeben oder Enter (default: 0.1kV über gesamtes Feld): "))
except:
    print("\n[*] Default: 0.1")
    error_threshold = 0.1
    pass

# Over-relaxation Wert abfragen (DEFAULT: 1.6)
try:
    relaxation = float(input("\nOver-relaxation Wert (zwischen 0 und 2) eingeben oder Enter (default: 1.6): "))
    if relaxation >= 2 and relaxation <= 0:
        relaxation = 1.6
        print("\n[*] nicht in Intervall! Default: 1.6")
except:
    print("\n[*] Default: 1.6")
    relaxation = 1.6
    pass


# Warte auf Enter um Berechnung zu starten
try:
    input("\n[*] Alle Daten geladen\n\nEnter um Berechnung zu starten")
except:
    pass


# Führe Iterationen aus
Z, iteration_count, total_error, total_error_mean, calc_time, error_entwicklung = it.iterativeLaplace(Z, relaxation, error_threshold)

# Zeige Details zur Berechnung an
print("\nBenötigte Zeit(in s): " + str(calc_time))
print("\nBenötigte Iterationen: " + str(iteration_count))
print("\nGesamter Fehler (letzter Schritt): " + str(total_error))
print("\nDurchschnittlicher Fehler (letzter Schritt): " + str(total_error_mean))
print("\nPotentialwert an der Stelle x=10 y=0: " + str(Z[51][41]))

# Zeige Ergebnis der Berechnung
plt.plot(X, Y, Z, error_entwicklung)
