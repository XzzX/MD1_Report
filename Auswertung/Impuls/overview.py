import sys
import numpy as np
import matplotlib.pyplot as pl

t, x, y, z, vx, vy, vz, ekin, epot, d, d2 = np.loadtxt(sys.argv[1]).transpose()

pl.figure(figsize=(16, 12))

pl.subplot(221)
pl.title("Schwerpunkt")
pl.plot(x,y, 'o-')
pl.xlabel("x")
pl.ylabel("y")
pl.legend()
pl.grid()

pl.subplot(222)
pl.title("Gesamtimpuls")
pl.plot(vx, vy, 'o-')
pl.xlabel("x")
pl.ylabel("y")
pl.legend()
pl.grid()

pl.subplot(223)
pl.title("Energie")
#pl.plot(t, ekin, label="Ekin")
#pl.plot(t, epot, label="Epot")
pl.plot(t, (ekin+epot)*0.5, 'o-', label="0.5*Eges")
pl.xlabel("Zeit")
pl.ylabel("Energie")
pl.legend(loc="upper left")
pl.grid()

pl.subplot(224)
pl.title("Diffusion")
pl.plot(t, d, label="d")
pl.plot(t, d2, label="d2")
pl.axhline(30.0*30.0)
pl.loglog()
pl.xlabel("Zeit")
pl.ylabel("Diffusion")
pl.legend(loc="upper left")
pl.grid()
pl.show()

Lx = 41.7556
Ly = 36.3419
N = 961.0

r = np.loadtxt("corraw_"+sys.argv[1]).transpose()
r[0] = 0.0
[h,x] = np.histogram(r,2000)
g = h*Lx*Ly/(np.pi*x[1]*x[1]*N*N*(np.arange(len(h))+1-0.5))
pl.plot(x[1:], g)
pl.xlim(0,15)
pl.xlabel("Abstand r")
pl.ylabel("Zwei-Punkt-Korrelationsfunktion g")
pl.show()