#!/bin/python3
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

res = np.loadtxt('res.csv', delimiter=',')
fig, ax = plt.subplots()

nodes = [int(elem) for elem in res[:, 0]]
ax.plot(nodes, res[:, 1], color='green', label='C')
ax.plot(nodes, res[:, 2], color='yellow', label='L2')
ax.legend(fontsize=10)
plt.xticks(nodes)
plt.grid()
plt.yscale('log')
plt.xscale('log', base=2)
plt.xlabel('number_of_nodes', fontsize=12)
fig.savefig('res.pdf', format='pdf', transparent=True)
