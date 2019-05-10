import numpy as np
import matplotlib.pyplot as plt

def indices_zero_grid(m,n):
     I,J = np.ogrid[:m,:n]
     out = np.zeros((m,n,3), dtype=float)
     out[...,0] = I
     out[...,1] = J
     return out

def plotlist(T):
    h, w = 120, 120
    out = indices_zero_grid(h, w)
    out[..., 2] = np.array(T)
    plt.imshow(out[..., 2])
    plt.show()
