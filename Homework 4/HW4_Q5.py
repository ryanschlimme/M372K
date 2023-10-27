import numpy as np
import matplotlib.pyplot as plt

def Fourier(x, n):
    a0 = 0
    f = np.array([((-1)**(1-i)/(1-i) - (-1)**(1+i)/(1+i))
                   *np.sin(i*x) for i in range(2, n+1)])
    f = np.append(f, -1/2*np.sin(x))
    return f.sum() + a0


xvals = np.linspace(-3*np.pi, 3*np.pi, 1000)
xvals1 = np.linspace(-np.pi, np.pi, 1000)

y1 = np.array([Fourier(x,3) for x in xvals1])
y2 = np.array([Fourier(x,5) for x in xvals1])
y3 = np.array([Fourier(x,100) for x in xvals1])

plt.plot(xvals1, xvals1*np.cos(xvals1))
plt.plot(xvals1, y1, alpha = 0.4)
plt.plot(xvals1, y2, alpha = 0.4)
plt.plot(xvals1, y3, alpha = 0.4)
plt.legend(["Function", "M = 3", "M = 5", "M = 30"])
#plt.show()
plt.savefig("Q5.png")