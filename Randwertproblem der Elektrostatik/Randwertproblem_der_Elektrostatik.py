import Iterative as it
from array import *
import random
from numpy.random import seed
from numpy.random import rand

# Initialisiere Array für Box
# Größe 50x50 
# Innere Größe 100x100
# Werte werden als float per numpy generiert 

import matplotlib.pyplot as plt
import numpy as np
seed(1)
x = np.linspace(-11,41, num=52)
y = np.linspace(-24,26, num=52)

X, Y = np.meshgrid(x,y)
Z = np.zeros((52,52))

for i in range(52):
   for j in range(52):
       Z[i,j] = rand()*100

#DEBUG
#plt.pcolor(X, Y, Z)
#plt.show()

print("[*] Array initialisiert \n")

#Initialisiere Äußeren Leiter
#jeweils 1 Block oben und seitlich
#Potential außen = 0*100000V
#Innere Anordung wird nach User Eingabe initialisiert

i = 0
B = []
while i < 52:
    B.insert(i, 0)
    i += 1

Z[0] = B
Z[50] = B

i = 0
while i < 52:
    Z[i][0] = 0
    Z[i][50] = 0
    i += 1

#DEBUG
#plt.pcolor(X, Y, Z)
#plt.show()
print("[*] Äußerer Leiter initialisiert\n")

#User Abfrage 
#Welche Szenario soll berechnet werden
#A/B/C vgl. Aufgabenblatt

abc = input("Welche Anordnung soll berechnet werden (A/B/C): ")

#Generiert geladene Fläche (4x4)
#Diese Fläche ist bei allen Szenarios gleich

i = 23
j = 9
while i < 27:
    while j < 13:
        Z[i][j]=100
        j +=1
    j = 9
    i += 1
#DEBUG
#plt.pcolor(X, Y, Z)
#plt.show()

#Szenario wird generiert
#Szenario A muss nicht weiter verändert werden

if abc == "B":
    i = 5
    while i < 45:
        Z[i][25] = 0
        i += 1
elif abc == "C":
    i = 23
    j = 38
    while i < 27:
        while j < 42:
            Z[i][j]=-100
            j +=1
        j = 38
        i += 1
else:
    print("\nERROR")
    exit(1)

try:
    input("\n[*] Alle Daten geladen\n\nEnter um Berechnung zu starten")
except SyntaxError:
    pass
Z=it.iterativeLaplace(Z,1000)
plt.pcolormesh(X, Y, Z)
plt.show()


