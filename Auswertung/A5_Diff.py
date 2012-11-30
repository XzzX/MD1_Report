# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as pl

t, x, y, z, vx, vy, vz, ekin, epot, d, d2 = np.loadtxt("Impuls/"+sys.argv[1]).transpose()
#t2, x2, y2, z2, vx2, vy2, vz2, ekin2, epot2, d3, d23 = np.loadtxt("NoImpuls/"+sys.argv[1]).transpose()

pl.title("lineare Diffusion")
pl.plot(t, d, label="kein Gesamtimpuls")
#pl.plot(t2, d3, label="mit Gesamtimpuls")
#pl.axhline(42.0*42.0)
#pl.loglog()
pl.xlabel("Zeit t [a.u.]")
pl.ylabel(ur"Diffusion $\left< \left[\vec{r}(t)-\vec{r}(0)\right] \right>$")
pl.legend(loc="upper left")
pl.grid()
pl.savefig("DiffL14L.png", dpi=300)
pl.show()

pl.title("Diffusion")
pl.plot(t, d2, label="kein Gesamtimpuls")
#pl.plot(t2, d23, label="mit Gesamtimpuls")
pl.loglog()
pl.xlabel("Zeit t [a.u.]")
pl.ylabel(ur"Diffusion $\left< \left[\vec{r}(t)-\vec{r}(0)\right]^2 \right>$")
pl.legend(loc="lower right")
pl.axhline(42.0*42.0)
pl.grid()
pl.savefig("DiffL14.png", dpi=300)
pl.show()