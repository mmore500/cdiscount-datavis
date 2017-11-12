import matplotlib.pyplot as plt
import numpy as np
import csv
import os

# open data

res1, res2, res3 = None, None, None

with open('data/level_1-2_cat_breakdown.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        res1 = np.array([x[1] for x in reader]).astype(np.float)

with open('data/level_1-3_cat_breakdown.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        res2 = np.array([x[1] for x in reader]).astype(np.float)

with open('data/level_2-3_cat_breakdown.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        res3 = np.array([x[1] for x in reader]).astype(np.float)

fs = 10  # fontsize

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(6, 6))

ybounds = list()

axes[0].violinplot([res1], [0], showextrema=True, showmedians=True)
axes[0].set_title('Level 2 per Level 1', fontsize=fs)
ybounds.append(axes[0].get_ylim())

axes[2].violinplot([res2], [0], showextrema=True, showmedians=True)
axes[2].set_title('Level 3 per Level 1', fontsize=fs)
ybounds.append(axes[2].get_ylim())

axes[1].violinplot([res3], [0], showextrema=True, showmedians=True)
axes[1].set_title('Level 3 per Level 2', fontsize=fs)
ybounds.append(axes[1].get_ylim())

res = list(zip(*ybounds))
ymin = min(res[0])
ymax = max(res[1])

for ax in axes:
    ax.set_ylim((ymin, ymax))
    ax.get_xaxis().set_ticks([])


fig.suptitle("Subcategory Counts")

fig.subplots_adjust(wspace=0.4)

if not os.path.exists('out'):
    os.makedirs('out')
plt.savefig('out/catcount.pdf', format='pdf')
