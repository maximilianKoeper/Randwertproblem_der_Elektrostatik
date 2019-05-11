#Iterative Berechnung der Laplacegleichung

#Berechnung wird von beiden Seiten vorgenommen um die Konvergenzgeschwindigkeit zu erhöhen
#Blöcke mit den Werten 0,100,-100 kV werden nicht überschrieben

def iterativeLaplace(V,d):
    x=0
    print("\n[ ] Iteration wird durchgeführt")

    while x < d/2:
        i = 0
        while i<50:
            j=0
            while j<50:
                if V[i][j] !=0 and V[i][j] != 100 and V[i][j] !=-100:
                    V[i][j]=(V[i-1][j]+V[i+1][j]+V[i][j-1]+V[i][j+1])/4
                j +=1
            i += 1
        i=50
        while i>0:
            j=50
            while j>0:
                if V[i][j] !=0 and V[i][j] != 100 and V[i][j] !=-100:
                    V[i][j]=(V[i-1][j]+V[i+1][j]+V[i][j-1]+V[i][j+1])/4
                j -=1
            i -= 1
        x += 1
    return V