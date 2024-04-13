"""
read `Average per episode return` logs from rainbow.out
"""

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os

dire = 'rainbow_results/'

for fname in os.listdir(dire):
    with open(dire + fname) as f:
        if not fname.endswith('.txt'): continue

        returns = []
        for line in f.readlines():
            if 'tensorflow:Average per episode return' in line:
                returns.append(float(line.split()[-1]))
        plt.plot(returns, label=fname[:-4])

plt.legend()
plt.savefig(dire + 'plot.png')

"""
with open('debug.txt') as f:
    returns = []
    for line in f.readlines():
        if 'tensorflow:Average per episode return' in line:
            returns.append(float(line.split()[-1]))
    print(returns)

# plot returns
plt.plot(returns)
# save plot
plt.savefig('debug.png')
"""