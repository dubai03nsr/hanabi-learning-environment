"""
read `Average per episode return` logs from rainbow.out
"""


with open('rainbow.out') as f:
    returns = []
    for line in f.readlines():
        if 'tensorflow:Average per episode return' in line:
            returns.append(float(line.split()[-1]))
    print(returns)
