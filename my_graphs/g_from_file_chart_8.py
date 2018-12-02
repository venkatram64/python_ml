import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []

x, y = np.loadtxt('chart_file.txt', delimiter=',', unpack=True)

plt.bar(x, y, label="BARS1")

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

