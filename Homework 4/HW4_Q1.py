import numpy as np
import matplotlib.pyplot as plt

def Fourier(x, n):
    a0 = 2/np.pi
    f = np.array([-1/np.pi * 
                  (1/(i+1)*(np.cos((i+1)*np.pi)-1)
                   -1/(i-1)*(np.cos((i+1)*np.pi)-1))
                   *np.cos(i*x) for i in range(2, n+1)])
    return f.sum() + a0


xvals = np.linspace(-np.pi, np.pi, 1000)
xvals1 = np.linspace(-np.pi, np.pi, 1000)

y1 = np.array([Fourier(x,3) for x in xvals])
y2 = np.array([Fourier(x,5) for x in xvals])
y3 = np.array([Fourier(x,30) for x in xvals])

plt.plot(xvals1, np.abs(np.sin(xvals1)))
plt.plot(xvals, y1, alpha = 0.4)
plt.plot(xvals, y2, alpha = 0.4)
plt.plot(xvals, y3, alpha = 0.4)
plt.legend(["Function", "M = 3", "M = 5", "M = 30"])
plt.savefig("Q1.png")