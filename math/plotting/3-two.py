mport numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)
plt.plot(x, y)
plt.xlabel("Time(Years)")
plt.ylabel("Fraction Remaining")
plt.title("Exponential Decay of C-14")
plt.xlim(0, 28650)
plt.yscale("log")
plt.show()
