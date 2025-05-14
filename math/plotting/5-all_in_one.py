mport numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 10))
# plot 1
axes[0, 0].plot(y0, 'r-')
axes[0, 0].set_xlim(0, 10)
axes[0, 0].set_title('Plot 1')
# plot 2
axes[0, 1].scatter(x1, y1, c='m')
axes[0, 1].set_xlabel('Height (in)', fontsize='x-small')
axes[0, 1].set_ylabel('Weight (lbs)', fontsize='x-small')
axes[0, 1].set_title("'Men's Height vs Weight'")
# plot 3
axes[1, 0].plot(x2, y2)
axes[1, 0].set_xlabel("Time (Years)", fontsize='x-small')
axes[1, 0].set_ylabel("Fraction Remaining", fontsize='x-small')
axes[1, 0].set_title("Exponential Decay of C-14")
axes[1, 0].set_xlim(0, 28650)
axes[1, 0].set_yscale("log")
# plot 4
axes[1, 1].hist(student_grades, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], edgecolor='black')
axes[1, 1].set_xlabel("Grades", fontsize='x-small')
axes[1, 1].set_ylabel("Number of Students", fontsize='x-small')
axes[1, 1].set_title("Project A")
axes[1, 1].set_xlim(0, 100)
axes[1, 1].set_xticks(np.arange(0, 101, 10))
axes[1, 1].set_ylim(0, 30)

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

axes[2, 0].plot(x, y1, 'r--', label='C-14')  # Dashed red line for C-14
axes[2, 0].plot(x, y2, 'g-', label='Ra-226')  # Solid green line for Ra-226
axes[2, 0].set_xlabel("Time (Years)", fontsize='x-small')
axes[2, 0].set_ylabel("Fraction Remaining", fontsize='x-small')
axes[2, 0].set_title("Exponential Decay of C-14 and Ra-226")
axes[2, 0].set_xlim(0, 20000) 
axes[2, 0].set_ylim(0, 1)     
axes[2, 0].legend(loc='upper right')
fig.suptitle("All in One", fontsize=16)
fig.delaxes(axes[2, 1])
plt.tight_layout()
plt.show()
