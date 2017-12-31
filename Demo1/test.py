# -*- coding: utf-8 -*-
import kNN
import numpy as np
import matplotlib.pyplot as plt
from random import randint
group1, labels1 = kNN.createDataSet()
group2, labels2 = kNN.createDataSet()
group3, labels3 = kNN.createDataSet()
group = np.vstack((group1, group2, group3))
labels = ['Red'] * 4 + ['Blue'] * 4 + ['Green'] * 4
plt.plot(group1[:, 0], group1[:, 1], 'or')
plt.plot(group2[:, 0], group2[:, 1], '1b')
plt.plot(group3[:, 0], group3[:, 1], 'Dg')
inX = [randint(0, 100), randint(0, 100)]
print inX
print kNN.classify0(inX, group, labels, 2)
plt.show()
