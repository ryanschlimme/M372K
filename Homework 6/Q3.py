import numpy as np
import matplotlib.pyplot as plt

def Fourier(x, t = 0, i = 1):
    a0 = 0.5*np.sin(np.pi*x)*np.cos(t)
    f = np.array([((-1)**(1-n)-1)/(np.pi)**2 * (1/(1-n)**2 - 1/(1+n)**2)
                   *np.sin(n*np.pi*x)*np.cos(n*t) for n in range(2, i+1)])
    f = np.append(f, a0)
    return f.sum()


xvals = np.linspace(0, 1, 1000)

y0 = np.array([Fourier(x, t = 0, i = 5) for x in xvals])
y1 = np.array([Fourier(x, t = 1, i = 5) for x in xvals])
y2 = np.array([Fourier(x, t = 10, i = 5) for x in xvals])
y3 = np.array([Fourier(x, t = 100, i = 5) for x in xvals])

plt.plot(xvals, xvals*np.sin(xvals*np.pi), label = "Function", color = "b")
plt.plot(xvals, y0, alpha = 0.4, label = "t = 0")
plt.plot(xvals, y1, alpha = 0.4, label = "t = 1")
plt.plot(xvals, y2, alpha = 0.4, label = "t = 10")
plt.plot(xvals, y3, alpha = 0.4, label = "t = 100")
plt.legend()
plt.title("M = 5")
#plt.show()
plt.savefig("Q3.png")