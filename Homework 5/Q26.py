import numpy as np
import matplotlib.pyplot as plt

def Fourier(x, i):
    a0 = 0
    f = np.array([((-2*np.pi)/n  *  (-1)**n   +   4/(n**3*np.pi) * ((-1)**n  -1))
                   *np.sin(n*x) for n in range(1, i+1)])
    f = np.append(f, a0)
    return f.sum()


xvals = np.linspace(-3*np.pi, 3*np.pi, 1000)

y0 = np.array([Fourier(x,1) for x in xvals])
y1 = np.array([Fourier(x,3) for x in xvals])
y2 = np.array([Fourier(x,5) for x in xvals])
y3 = np.array([Fourier(x,100) for x in xvals])

plt.plot(xvals, xvals**2, label = "Function", color = "b")
plt.plot(xvals, y0, alpha = 0.4, label = "M = 1")
plt.plot(xvals, y1, alpha = 0.4, label = "M = 3")
plt.plot(xvals, y2, alpha = 0.4, label = "M = 5")
plt.plot(xvals, y3, alpha = 0.4, label = "M = 30")
plt.legend()
#plt.show()
plt.savefig("Q26_3pi.png")