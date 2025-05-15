import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
fruit_labels = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
fig, ax = plt.subplots()
bottom = np.zeros(3)
for i, fruit_label in enumerate(fruit_labels):
    ax.bar(np.arange(3), fruit[i], bottom=bottom, color=colors[i], label=fruit_label, width=0.5)
    bottom += fruit[i]

ax.set_ylabel('Quantity of Fruit')
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))
ax.set_xticks(np.arange(3))
ax.set_xticklabels(['Farrah', 'Fred', 'Felicia'])
ax.set_title('Number of Fruit per Person')
ax.legend()

plt.show()
