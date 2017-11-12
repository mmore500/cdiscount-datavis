import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import csv

import os

# open data

res1, res2, res3 = None, None, None

with open('data/category_count_level1.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        res1 = np.array([x[1] for x in reader]).astype(np.float)

with open('data/category_count_level2.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        res2 = np.array([x[1] for x in reader]).astype(np.float)

with open('data/category_count_level3.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        res3 = np.array([x[1] for x in reader]).astype(np.float)

fs = 10  # fontsize
pos = [1, 2, 3]
data = [res1, res2, res3]

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 6))

axes.violinplot(data, pos, showextrema=True, showmedians=True)
axes.set_yscale('log')
axes.set_xlabel('Hierarchy Level')
axes.set_ylabel('Number Training Examples')

axes.xaxis.set_major_locator(MaxNLocator(integer=True))


fig.suptitle("Training Image Count by Category over Hierarchicial Levels")

fig.subplots_adjust(hspace=0.4)

if not os.path.exists('out'):
    os.makedirs('out')
plt.savefig('out/datacount.pdf', format='pdf')
