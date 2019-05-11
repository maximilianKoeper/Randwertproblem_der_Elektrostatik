import Iterative as it
import Plot as plt
from numpy.random import randint
import numpy as np

print("Randwertproblem der Elektrostatik\nVersion 1.1\n")

# Initialisiere Array für Box
# Größe 50x50 
# Innere Größe 100x100
# Werte werden als float per numpy generiert 
# Zufallswerte sind zwischen 1 und 99

x = np.linspace(-10,40, num=102)
y = np.linspace(-25,25, num=102)

X, Y = np.meshgrid(x,y, sparse=True ,copy=True)
Z = np.zeros((102,102), dtype=np.float)

for i in range(102):
   for j in range(102):
       Z[i,j] = float(randint(1, high=99, size=None))


print("[*] Array initialisiert \n")

#Initialisiere Äußeren Leiter
#jeweils 1 Block oben und seitlich
#Potential außen = 0*100000V
#Innere Anordung wird nach User Eingabe initialisiert

i = 0
B = []
while i < 102:
    B.insert(i, 0)
    i += 1

Z[0] = B
Z[100] = B

i = 0
while i < 102:
    Z[i][0] = 0
    Z[i][100] = 0
    i += 1

print("[*] Äußerer Leiter initialisiert\n")

#User Abfrage 
#Welche Szenario soll berechnet werden
#A/B/C vgl. Aufgabenblatt

abc = input("Welche Anordnung soll berechnet werden (A/B/C): ")

#Generiert geladene Fläche (4x4)
#Diese Fläche ist bei allen Szenarios gleich

i = 46
j = 18
while i < 54:
    while j < 26:
        Z[i][j]=100
        j +=1
    j = 18
    i += 1

#Szenario wird generiert
#Szenario A muss nicht weiter verändert werden

if abc == "B":
    i = 10
    while i < 90:
        Z[i][50] = 0
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
    print("\nERROR")
    #exit(1)


#Warte auf Enter
try:
    input("\n[*] Alle Daten geladen\n\nEnter um Berechnung zu starten")
except SyntaxError:
    pass

#Führe Iterationen aus
Z, iteration_count, total_error, total_error_mean, calc_time = it.iterativeLaplace(Z)

#Zeige Details zur Berechnung an
print("\nBenötigte Zeit(in s): " + str(calc_time))
print("\nBenötigte Iterationen: " + str(iteration_count))
print("\nGesamter Fehler (letzter Schritt): " + str(total_error))
print("\nDurchschnittlicher Fehler (letzter Schritt): " + str(total_error_mean))

#Zeige Ergebnis der Berechnung
plt.plot(X, Y, Z)