import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as pl

_t = 0
_x = 1
_y = 2
_z = 3
_vx = 4
_vy = 5
_vz = 6
_ekin = 7
_epot = 8
#A101 = np.loadtxt("Impuls/L1V05dt01.txt").transpose()
#A1001 = np.loadtxt("Impuls/L1V05dt001.txt").transpose()
#A1005 = np.loadtxt("Impuls/L1V05dt005.txt").transpose()

A101 = np.loadtxt("Impuls/L14V05.txt").transpose()
A1001 = np.loadtxt("Impuls/Eulerdt001.txt").transpose()
A1005 = np.loadtxt("Impuls/Eulerdt005.txt").transpose()

#pl.figure(figsize=(12, 9))

E101 = 0.5*A101[_x]**2 + 0.5*A101[_vx]**2
E1001 = 0.5*A1001[_x]**2 + 0.5*A1001[_vx]**2
E1005 = 0.5*A1005[_x]**2 + 0.5*A1005[_vx]**2

pl.title("Gesamtenergie")
pl.plot(A1001[_t], E1001, 'x', label = ur"$\Delta t = 0.01$")
pl.plot(A1005[_t], E1005, 'x', label = ur"$\Delta t = 0.05$")
pl.plot(A101[_t], E101, 'x', label = ur"$\Delta t = 0.1$")
pl.yscale("log")
pl.xscale("log")
pl.xlabel("Zeit t [a.u.]")
pl.ylabel("Energie E [a.u.]")
pl.legend(loc = "upper left")
pl.grid()

pl.savefig("A3EnergieEuler.png", dpi = 300)
pl.show()

#FitFunc = lambda a,b,x : a*x + b
#Residuals = lambda p, y, x: y - FitFunc(p[0], p[1], x)
#pGuess = [1.0, 1.0]
#kd,cov= optimize.leastsq(Residuals, pGuess, args=(np.log(E1001), A1001[_t]))
#print "0.01", kd

#kd,cov= optimize.leastsq(Residuals, pGuess, args=(np.log(E1005), A1005[_t]))
#print "0.5", kd

#kd,cov= optimize.leastsq(Residuals, pGuess, args=(np.log(E101), A101[_t]))
#print "0.1", kd