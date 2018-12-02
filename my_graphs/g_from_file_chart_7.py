import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('chart_file.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append((int(row[1])))


plt.bar(x, y, label="BARS1")

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

