import numpy as np
import matplotlib.pyplot as plt

def Fourier(x, n):
    a0 = 0.5
    f = np.array([-1/(i*np.pi)*((-1)**i +1)
                   *np.sin(np.pi * i*x) for i in range(1, n+1)])
    f = np.append(f, a0)
    return f.sum()


xvals = np.linspace(-1, 1, 1000)

y0 = np.array([Fourier(x,1) for x in xvals])
y1 = np.array([Fourier(x,3) for x in xvals])
y2 = np.array([Fourier(x,5) for x in xvals])
y3 = np.array([Fourier(x,30) for x in xvals])

xvals0 = np.linspace(-1, 0, 500)
xvals1 = np.linspace(0, 1, 500)

plt.plot(xvals0, 1 + xvals0, label = "Function", color = "b")
plt.plot(xvals1, xvals1, label = '', color = "b")
plt.plot(xvals, y0, alpha = 0.4, label = "M = 1")
plt.plot(xvals, y1, alpha = 0.4, label = "M = 3")
plt.plot(xvals, y2, alpha = 0.4, label = "M = 5")
plt.plot(xvals, y3, alpha = 0.4, label = "M = 30")
plt.legend()
#plt.show()
plt.savefig("Q7.png")