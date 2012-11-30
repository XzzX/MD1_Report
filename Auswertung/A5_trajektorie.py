import sys
import numpy as np
import matplotlib.pyplot as pl

rc=np.power(2.0,1.0/6.0)
N=961.0
LC = 1.4 * rc
a = np.array([1.0,0.0]) * LC
b = np.array([np.cos(np.pi/3.0),np.sin(np.pi/3.0)]) * LC

numa = (np.floor(np.sqrt(N)))
numb = numa

delta = np.array([LC,LC]) * 0.5;

x1 = np.zeros(0)
x2 = np.zeros(0)
for i in range(np.int(numa)):
	for j in range(np.int(numb)):
		x1 = np.append(x1, (i*a + j*b - np.floor(j/2.0)*a + delta)[0])
		x2 = np.append(x2, (i*a + j*b - np.floor(j/2.0)*a + delta)[1])
		
Ly = b[1] * (numb-1) + LC;
Lx = a[0] * (numa-1) + LC;


x = np.loadtxt("Impuls/rawpos_"+sys.argv[1]).transpose()

#pl.figure(figsize=(16, 12))

pl.title("Teilchentrajektorien")
for i in range(len(x1)):
	pl.plot(x1[i],x2[i], "x", color="k")
pl.plot(x[0], x[1], "x", label="Teilchen 0")
pl.plot(x[3], x[4], "x", label="Teilchen 1")
pl.plot(x[6], x[7], "x", label="Teilchen 2")
pl.plot(x[9], x[10], "x", label="Teilchen 3")
pl.plot(x[12], x[13], "x", label="Teilchen 4")
pl.plot(x[15], x[16], "x", label="Teilchen 5")
pl.plot(x[18], x[19], "x", label="Teilchen 6")
pl.plot(x[21], x[22], "x", label="Teilchen 7")
pl.plot(x[24], x[25], "x", label="Teilchen 8")
pl.plot(x[27], x[28], "x", label="Teilchen 9")

#Lx=48.7149
#Ly=42.3988

#Lx=27.8371
#Ly=24.2279

pl.xlabel("x")
pl.ylabel("y")
pl.xlim(0,Lx)
pl.ylim(0,Ly)
#pl.legend(loc="upper left")
pl.grid()
pl.show()