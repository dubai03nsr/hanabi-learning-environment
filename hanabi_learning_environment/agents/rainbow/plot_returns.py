"""
read `Average per episode return` logs from rainbow.out
"""

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os

dire = 'rainbow_results/'
# """

# for fname in os.listdir(dire):
# for fname in ['small-cheat.txt', 'small.txt']:
for fname in ['custom.txt', 'custom-cheat.txt']:
    with open(dire + fname) as f:
    # with open(fname) as f:
        if not fname.endswith('.txt'): continue

        returns = []
        for line in f.readlines():
            if 'tensorflow:Average per episode return' in line:
                returns.append(float(line.split()[-1]))
        plt.plot(returns, label=fname[:-4])

plt.legend()
plt.savefig(dire + 'custom.png')
# """

"""
# for fname in ['orig-small.txt']:
for fname in ['orig-small.txt']:
    # with open(dire + fname) as f:
    with open(fname) as f:
        if not fname.endswith('.txt'): continue

        returns = [0] * 10
        for line in f.readlines():
            if 'tensorflow:EPISODE: ' in line:
                returns[int(line.split()[-1])] += 1
                # max_return = max(max_return, int(line.split()[-1]))
        # print(returns)
        plt.plot(returns, label=fname[:-4])

plt.legend()
plt.savefig(dire + 'custom.png')
"""