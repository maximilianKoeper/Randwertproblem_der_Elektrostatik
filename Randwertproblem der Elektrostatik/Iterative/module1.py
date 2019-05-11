#Iterative Berechnung der Laplacegleichung

#Berechnung wird von beiden Seiten vorgenommen um die Konvergenzgeschwindigkeit zu erhöhen
#Blöcke mit den Werten 0,100,-100 kV werden nicht überschrieben
import copy

def iterativeLaplace(V):
    U = V.copy()
    total_error = float(0)
    print("\n[ ] Iteration wird durchgeführt")
    x = True
    iteration_count = 0
    o = 0

    while x == True:
        o = 0
        iteration_count += 1
        i = 0
        total_error = 0
        while i<50:
            j=0
            while j<50:
                if V[i][j] !=0 and V[i][j] != 100 and V[i][j] !=-100:
                    V[i][j]=float((V[i-1][j]+V[i+1][j]+V[i][j-1]+V[i][j+1])/4)
                j +=1
            i += 1
        i=50
        while i>0:
            j=50
            while j>0:
                if V[i][j] !=0 and V[i][j] != 100 and V[i][j] !=-100:
                    V[i][j]=float((V[i-1][j]+V[i+1][j]+V[i][j-1]+V[i][j+1])/4)
                j -=1
            i -= 1
        #Berechnung des Fehlers
        i = 0
        while i<50:
            j=0
            while j<50:
                total_error += abs(float(V[i][j] - U[i][j]))
                o += 1
                j +=1
            i += 1
        if total_error < 20:
            x = False
        U = V.copy()



    total_error_mean = float(total_error/o)
    return V, iteration_count, total_error, total_error_mean
