import Iterative as it
import Plot as pt
from array import *
import random
from numpy.random import seed
from numpy.random import rand

# Initialisiere Array für Box
# Größe 120x120 
# Innere Größe 100x100
# Werte werden als float per numpy generiert 

T = []
i = 0
seed(1)
while i < 120:
  B = rand(120)
  T.insert(i, B)
  i += 1

print("[*] Array initialisiert \n")

#Initialisiere Äußeren Leiter
#jeweils 10 Blöcke oben und seitlich
#Potential außen = 0*100000V
#Innere Anordung wird nach User Eingabe initialisiert

i = 0
B = []
while i < 120:
    B.insert(i, 0)
    i += 1

i = 0
while i < 10:
    T[i] = B
    T[119 - i] = B
    i += 1

i = 0
while i < 120:
    j=0
    while j < 10:
        T[i][j] = 0
        T[i][119-j] = 0
        j += 1
    i += 1

print("[*] Äußerer Leiter initialisiert\n")

#DEBUG
#Zeigt aktuelles Array mit Außenleiter
#pt.plotlist(T)

#User Abfrage 
#Welche Szenario soll berechnet werden
#A/B/C vgl. Aufgabenblatt

input = input("Welche Anordnung soll berechnet werden (A/B/C): ")
if input == "A":
    i = 55
    j = 25
    while i < 64:
        while j < 34:
            T[i][j]=1
            j +=1
        j = 25
        i += 1
elif input == "B":
    print("B")
elif input == "C":
    print("C")
else:
    print("ERROR")
    exit(1)

#DEBUG
#Zeigt aktuelles Array mit allen Leitern
pt.plotlist(T)
