#Iterative Berechnung der Laplacegleichung

#Berechnung wird von beiden Seiten vorgenommen um die Konvergenzgeschwindigkeit zu erhöhen
#Over-relaxation wird genutzt um die Konvergenzgeschwindigkeit weiter zu beschleunigen
#Blöcke mit den Werten 0,100,-100 kV werden nicht überschrieben (alle anderen Blöcke können diesen Wert nicht annehmen)

import copy
import time
import math

def iterativeLaplace(V, over_relaxation_value, error_threshold):
    a = time.perf_counter()
    total_error = float(0)
    print("\n[ ] Iterationen werden durchgeführt (Bitte warten)...")
    x = True
    iteration_count = 0
    error_entwicklung = []

    #Lese x,y Werte des Arrays aus
    V_x, V_y = V.shape

    #Starte Berechnung bis Fehler unter 0.1kV auf dem Gesamten Feld ist
    while x == True:
        iteration_count += 2
        total_error = 0
        #Altes Array in U kopieren um Over-relaxation berechnen zu können
        U = V.copy()
        
        #Starte 1. Iterationsdurchlauf (von links oben)
        i = 1
        while i<=(V_x-2):
            j=1
            while j<=(V_y-2):
                if V[i][j] !=0 and V[i][j] != 100 and V[i][j] !=-100:
                    #Potential für Punkt i,j
                    c = float((V[i-1][j]+V[i+1][j]+V[i][j-1]+V[i][j+1])/4) - float(U[i][j])
                    V[i][j] = float(U[i][j]) + c*over_relaxation_value
                j +=1
            i += 1
        
        #Altes Array kopieren 
        U = V.copy()
        
        #Starte 2. Iterationsdurchlauf (von rechts unten)
        i=(V_x-2)
        while i>0:
            j=(V_x-2)
            while j>0:
                if V[i][j] !=0 and V[i][j] != 100 and V[i][j] !=-100:
                    #Potential für Punkt i,j
                    c = float((V[i-1][j]+V[i+1][j]+V[i][j-1]+V[i][j+1])/4) - float(U[i][j])
                    V[i][j] = float(U[i][j]) + c*over_relaxation_value
                j -=1
            i -= 1
        
        #Berechnung des Fehlers
        for i in range((V_x)):
            for j in range((V_x)):
                total_error += abs(float(V[i][j] - U[i][j]))
        
        #Fehler in Liste eintragen um Fehlerentwicklung plotten zu können 
        error_entwicklung.append(math.log10(total_error))
        
        #Prüfe ob Fehler unter 0.1 Grenze liegt
        if total_error < error_threshold:
            x = False


    total_error_mean = float(total_error/(V_x*V_y))
    calc_time = time.perf_counter() - a
    return V, iteration_count, total_error, total_error_mean, calc_time, error_entwicklung
