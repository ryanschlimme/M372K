import numpy as np
import matplotlib.pyplot as plt

xvals = np.linspace(0, 1, 1000)

plt.plot(xvals, 0.5*np.sin(np.pi*xvals), label = "Function", color = "b")
plt.plot(xvals, 0.5*np.sin(np.pi*xvals), alpha = 0.4, label = "M = 1, t = 0")
plt.plot(xvals, 0.5*np.sin(np.pi*xvals)*np.cos(1), alpha = 0.4, label = "M = 1, t = 1")
plt.plot(xvals, 0.5*np.sin(np.pi*xvals)*np.cos(10), alpha = 0.4, label = "M = 1, t = 10")
plt.plot(xvals, 0.5*np.sin(np.pi*xvals)*np.cos(100), alpha = 0.4, label = "M = 1, t = 100")
plt.legend()
#plt.show()
plt.savefig("Q1.png")