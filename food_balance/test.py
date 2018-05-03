
import numpy as np
import matplotlib.pylab as pl
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 64)
y = np.cos(x)

pl.figure()
pl.plot(x,y)

n = 20
colors = pl.cm.Blues(np.linspace(0,1,n))

for i in range(n):
    pl.plot(x, i*y, color=colors[i],label = colors[i])

plt.legend()
plt.show()
