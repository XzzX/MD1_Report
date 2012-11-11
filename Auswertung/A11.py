import numpy as np
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
A1R01 = np.loadtxt("1R01.txt").transpose()
A1R1 = np.loadtxt("1R1.txt").transpose()
A1R10 = np.loadtxt("1R10.txt").transpose()

A = 5.61231
omega = 1.0
gamma = 1.0
alpha = np.sqrt(gamma**2-omega**2)
HarmOszi = lambda t : A*np.cos(omega*t)
HarmOsziSch = lambda t : A*np.exp(-gamma*t)*np.cos(omega*t)
HarmOsziA = lambda t : A*(1+gamma*t)*np.exp(-gamma*t)
HarmOsziSt = lambda t : A/alpha*np.exp(-gamma*t)*(alpha*np.cosh(alpha*t)+gamma*np.sinh(alpha*t))

#pl.figure(figsize=(12, 9))

gamma = 0.1
pl.title(ur"schwache Dämpfung")
pl.plot(A1R01[_t], A1R01[_x], 'x')
pl.plot(A1R01[_t], HarmOsziSch(A1R01[_t]), linewidth=2)
pl.xlabel("Zeit t [a.u.]")
pl.ylabel("Position x [a.u.]")
pl.legend(loc = "upper left")
pl.grid()
pl.show()

gamma = 1.0
pl.title("aperiodischer Grenzfall")
pl.plot(A1R1[_t], A1R1[_x], 'x')
pl.plot(A1R1[_t], HarmOsziA(A1R1[_t]), linewidth=2)
pl.xlabel("Zeit t [a.u.]")
pl.ylabel("Position x [a.u.]")
pl.legend(loc = "upper left")
pl.grid()
pl.show()

gamma = 10.0
alpha = np.sqrt(gamma**2-omega**2)
pl.title(ur"starke Dämpfung")
pl.plot(A1R10[_t], A1R10[_x], 'x')
pl.plot(A1R10[_t], HarmOsziSt(A1R10[_t]), linewidth=2)
pl.xlabel("Zeit t [a.u.]")
pl.ylabel("Position x [a.u.]")
pl.legend(loc = "upper left")
pl.grid()
pl.show()

