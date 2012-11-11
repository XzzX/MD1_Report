import numpy as np
import matplotlib.pyplot as pl

sigma = 1.0
epsilon = 1.0

LJ = lambda r : 4.0*epsilon*( (sigma/r)**12-(sigma/r)**6)

rc = 2.0**(1.0/6.0)*sigma

#pl.figure(figsize=(12, 9))

d = np.arange(0.0, 2.0*rc, rc*0.01)

pl.title(ur"Lennard-Jones-Potential")
epsilon = 1.0
pl.plot(d, LJ(d), label = ur"$\epsilon = 1.0$")
pl.ylim(-2.5*epsilon, 10*epsilon)
epsilon = 1.5
pl.plot(d, LJ(d), label = ur"$\epsilon = 1.5$")
epsilon = 2.0
pl.plot(d, LJ(d), label = ur"$\epsilon = 2.0$")
pl.axvline(rc, linestyle='--', color="k")
pl.text(rc+0.05, 9.0, ur"$r_c = 2^\frac{1}{6}\sigma$")
pl.xlabel("Distanz d [a.u.]")
pl.ylabel("Energie E [a.u.]")
pl.legend(loc = "upper right")
pl.grid()
pl.show()

d = np.arange(0.0, 4.0*rc, rc*0.01)

pl.title(ur"Lennard-Jones-Potential")
sigma = 1.0
rc = 2.0**(1.0/6.0)*sigma
pl.plot(d, LJ(d), label = ur"$\sigma = 1.0$")
pl.ylim(-2.5*epsilon, 10*epsilon)
sigma = 1.5
rc = 2.0**(1.0/6.0)*sigma
pl.plot(d, LJ(d), label = ur"$\sigma = 1.5$")
sigma = 2.0
rc = 2.0**(1.0/6.0)*sigma
pl.plot(d, LJ(d), label = ur"$\sigma = 2.0$")
pl.xlabel("Distanz d [a.u.]")
pl.ylabel("Energie E [a.u.]")
pl.legend(loc = "upper right")
pl.grid()
pl.show()

