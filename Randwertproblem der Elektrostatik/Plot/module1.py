import matplotlib.pyplot as plt

#Erstellt eine graphische Übersicht der Berechneten Daten sowie der Fehler Entwicklung
#Plot 1: Raw Daten
#Plot 2: Daten Interpoliert
#Plot 3: Äquipotentiallinien
#Plot 4: Gesamte Fehlerentwicklung

def plot(X, Y, Z, error_entwicklung):
    plt.subplot(2,2,1)
    plt.suptitle('Randwertproblem der Elektrostatik\nWert an P(10,0) (in kV): ' + str(round((Z[51][41]),4)) , fontsize=16)
    plt.title('Ergebnis')
    plt.pcolormesh(X, Y, Z, shading='flat')
    plt.colorbar()
    plt.subplot(2,2,2)
    plt.title('Interpoliert')
    plt.pcolormesh(X, Y, Z, shading='gouraud')
    plt.colorbar()
    plt.subplot(2,2,3)
    plt.title('Äquipotentiallinien')
    plt.contour(Z, levels=25)
    plt.colorbar()
    plt.subplot(2,2,4)
    plt.title('Fehler Entwicklung Gesamt (logarithmisch)')
    plt.plot(error_entwicklung, 'bo')
    plt.xlabel('Iteration (x2)')
    plt.ylabel('log10(kV)')
    plt.tight_layout()
    plt.show()

