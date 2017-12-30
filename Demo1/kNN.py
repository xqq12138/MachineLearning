# -*- coding: utf-8 -*-
import numpy as np
from random import randint
import operator


def createRand(range_=100, num_=2):
    return [randint(0, range_) for i in range(num_)]


def createDataSet():
    group = np.array([
        createRand(),
        createRand(),
        createRand(),
        createRand(),
    ])
    labels = ['A', 'B', 'C', "D"]
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # 计算输入点与样本的距离(x, y)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    # 排序索引
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in xrange(k):
        voteIlable = labels[sortedDistIndicies[i]]
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1
    sortClassCount = sorted(classCount.iteritems())
    return sortClassCount[0][0]
