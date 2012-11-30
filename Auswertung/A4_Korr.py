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
		
Ly = b[1] * (numb-1) + LC;
Lx = a[0] * (numa-1) + LC;

LC = 1.0 * rc
a = np.array([1.0,0.0]) * LC
b = np.array([np.cos(np.pi/3.0),np.sin(np.pi/3.0)]) * LC

N = 961.0

r = np.loadtxt("Impuls/corraw_"+sys.argv[1]).transpose()
[h,x] = np.histogram(r,2000, range=(0,r.max()))
g = h*Lx*Ly/(np.pi*x[1]*x[1]*N*N*(np.arange(len(h))+1-0.5))
for i in range(1,11):
	for j in range(i/2+1):
		c = (i-j)*a + b*j
		pl.axvline(np.sqrt(c[0]*c[0]+c[1]*c[1]), color="r")
pl.plot(x[1:], g)
pl.grid()
pl.xlim(0,15)
pl.xlabel("Abstand r")
pl.ylabel("Zwei-Punkt-Korrelationsfunktion g")
pl.title("Gitterkonstante = 1.4")
pl.show()