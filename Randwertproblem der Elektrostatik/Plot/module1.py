import matplotlib.pyplot as plt

def plot(X, Y, Z):
    plt.title('Randwertproblem der Elektrostatik')
    plt.pcolormesh(X, Y, Z)
    plt.show()
