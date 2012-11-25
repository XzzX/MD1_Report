import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as optimize

lz = np.loadtxt("laufzeit.txt").transpose()

FitFunc = lambda a,b,x : a*x + b
Residuals = lambda p, y, x: y - FitFunc(p[0], p[1], x)
pGuess = [1.0, 1.0]
kd,cov= optimize.leastsq(Residuals, pGuess, args=(np.log(lz[1][-17:]), np.log(lz[0][-17:])))

pl.title(ur"Laufzeit")
pl.errorbar(lz[0], lz[1], lz[2], fmt="x", label = ur"Messdaten")
pl.plot(lz[0], lz[0]**kd[0]*np.exp(kd[1]), label = ur"bestimmte Komplexität", linewidth=2)
pl.xscale("log")
pl.yscale("log")
pl.xlabel("Teilchenzahl")
pl.ylabel("Laufzeit pro Integrationsschritt in [ns]")
pl.legend(loc = "upper left")
pl.grid()
pl.show()

print kd

lz = np.loadtxt("laufzeit2.txt").transpose()

FitFunc = lambda a,b,x : a*x + b
Residuals = lambda p, y, x: y - FitFunc(p[0], p[1], x)
pGuess = [1.0, 1.0]
kd,cov= optimize.leastsq(Residuals, pGuess, args=(np.log(lz[1][-17:]), np.log(lz[0][-17:])))

pl.title(ur"Laufzeit")
pl.errorbar(lz[0], lz[1], lz[2], fmt="x", label = ur"Messdaten")
pl.plot(lz[0], lz[0]**kd[0]*np.exp(kd[1]), label = ur"bestimmte Komplexität", linewidth=2)
pl.xscale("log")
pl.yscale("log")
pl.xlabel("Teilchenzahl")
pl.ylabel("Laufzeit pro Integrationsschritt in [ns]")
pl.legend(loc = "upper left")
pl.grid()
pl.show()

print kd


