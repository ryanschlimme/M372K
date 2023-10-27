import numpy as np
import matplotlib.pyplot as plt

def Fourier(x, i):
    a0 = 1/3
    f = np.array([(4*(-1)**n) / ((n * np.pi) ** 2)
                   *np.cos(np.pi * n*x) for n in range(1, i+1)])
    f = np.append(f, a0)
    return f.sum()


xvals = np.linspace(-1, 1, 1000)

y0 = np.array([Fourier(x,1) for x in xvals])
y1 = np.array([Fourier(x,3) for x in xvals])
y2 = np.array([Fourier(x,5) for x in xvals])
y3 = np.array([Fourier(x,7) for x in xvals])

plt.plot(xvals, xvals**2, label = "Function", color = "b")
plt.plot(xvals, y0, alpha = 0.4, label = "M = 1")
plt.plot(xvals, y1, alpha = 0.4, label = "M = 3")
plt.plot(xvals, y2, alpha = 0.4, label = "M = 5")
plt.plot(xvals, y3, alpha = 0.4, label = "M = 7")
plt.legend()
#plt.show()
plt.savefig("Q18.png")