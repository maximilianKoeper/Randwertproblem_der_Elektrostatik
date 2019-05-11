import matplotlib.pyplot as plt

def plot(X, Y, Z, error_entwicklung):
    plt.subplot(2,2,1)
    plt.suptitle('Randwertproblem der Elektrostatik', fontsize=16)
    plt.title('Ergebnis')
    plt.pcolormesh(X, Y, Z, shading='flat')
    plt.subplot(2,2,2)
    plt.title('Interpoliert')
    plt.pcolormesh(X, Y, Z, shading='gouraud')
    plt.subplot(2,2,3)
    plt.title('Äquipotentiallinien')
    plt.contour(Z, levels=25)
    plt.subplot(2,2,4)
    plt.title('Fehler Entwicklung Gesamt (logarithmisch)')
    plt.plot(error_entwicklung, 'bo')
    plt.xlabel('Iteration (x2)')
    plt.ylabel('log10(kV)')
    plt.tight_layout()
    plt.show()

