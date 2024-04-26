"""
read `Average per episode return` logs
"""

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

dire = 'rainbow_results/'
fnames = ['cheat.txt', 'base.txt', 'tom0.txt', 'tom1.txt']
plot_names = [r'cheat$_0$', 'base', r'ToM$_0$', r'ToM$_1$']

for fname_i, fname in enumerate(fnames):
    with open(dire + fname) as f:
        if not fname.endswith('.txt'): continue

        returns = []
        for line in f.readlines():
            if 'tensorflow:Average per episode return' in line:
                returns.append(float(line.split()[-1]))
        plt.plot(returns, label=plot_names[fname_i], linewidth=1)
        print(len(returns))
        # print average of last 100 returns
        print(fname, sum(returns[-50:]) / 50)

plt.legend()
plt.title('Training trajectories in 2-player Hanabi')
plt.xlabel('iteration')
plt.ylabel('avg return')
plt.savefig(dire + 'results.png')