import sys
import numpy as np
import matplotlib.pyplot as pl

pl.figure(figsize=(16, 12))

Lx = 48.7149
Ly = 42.3988
N = 961.0

r = np.loadtxt("Impuls/corraw_"+sys.argv[1]).transpose()
[h,x] = np.histogram(r,2000, range=(0,r.max()))
g = h*Lx*Ly/(np.pi*x[1]*x[1]*N*N*(np.arange(len(h))+1-0.5))
pl.plot(x[1:], g)
pl.grid()
pl.xlim(0,15)
pl.xlabel("Abstand r")
pl.ylabel("Zwei-Punkt-Korrelationsfunktion g")
pl.title("Gitterkonstante = 1.4")
pl.show()