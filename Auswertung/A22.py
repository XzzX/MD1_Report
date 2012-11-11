import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as optimize

lz = np.loadtxt("laufzeit.txt").transpose()

FitFunc = lambda a,b,c,d,x : a*x*x*x + b*x*x + c*x + d
Residuals = lambda p, y, x: y - FitFunc(p[0], p[1], p[2], p[3], x)
pGuess = [1.0, 1.0, 1.0, 1.0]
kd,cov= optimize.leastsq(Residuals, pGuess, args=(lz[1], lz[0]))

pl.title(ur"Laufzeit")
pl.errorbar(lz[0], lz[1], lz[2], label = ur"Messdaten")
pl.plot(lz[0], FitFunc(kd[0],kd[1],kd[2],kd[2],lz[0]), label = ur"Polynomfit 3. Grades")
pl.xlabel("Teilchenzahl")
pl.ylabel("Laufzeit pro Integrationsschritt in [ns]")
pl.legend(loc = "upper left")
pl.grid()
pl.show()


