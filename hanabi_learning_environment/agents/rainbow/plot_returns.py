"""
read `Average per episode return` logs from rainbow.out
"""

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

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
