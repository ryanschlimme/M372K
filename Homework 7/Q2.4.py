import numpy as np
import matplotlib.pyplot as plt

def FourierTransform(w):
    return 1/(2*np.pi*w*1j)*(np.exp(5*w*1j)-np.exp(3*w*1j))

xvals = np.linspace(-5, 5, 1000)

fig, (ax0, ax1) = plt.subplots(2,1, sharex = True)

ax0.plot(xvals, np.real(FourierTransform(xvals)), color = "b")
ax1.plot(xvals, np.imag(FourierTransform(xvals)), color = "r")

fig.suptitle("Fourier Transform (F($\omega$))")
ax0.set_xlabel("$\omega$ (rad/s)")
ax0.set_ylabel("$\Re$(F($\omega$))")
ax1.set_xlabel("$\omega$ (rad/s)")
ax1.set_ylabel("$\Im$(F($\omega$))")
#plt.show()
plt.savefig("Q2.4.png")