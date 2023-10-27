import numpy as np
import matplotlib.pyplot as plt

xvals = np.linspace(0, 1, 1000)

plt.plot(xvals, 0.5*np.sin(2*np.pi*xvals), label = "Function", color = "b")
plt.plot(xvals, 0.5*np.sin(2*np.pi*xvals), alpha = 0.4, label = "M = 2, t = 0")
plt.plot(xvals, 0.5*np.sin(2*np.pi*xvals)*np.cos(2), alpha = 0.4, label = "M = 2, t = 1")
plt.plot(xvals, 0.5*np.sin(2*np.pi*xvals)*np.cos(20), alpha = 0.4, label = "M = 2, t = 10")
plt.plot(xvals, 0.5*np.sin(2*np.pi*xvals)*np.cos(200), alpha = 0.4, label = "M = 2, t = 100")
plt.legend()
#plt.show()
plt.savefig("Q2.png")