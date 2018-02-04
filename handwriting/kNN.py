# -*- coding: utf-8 -*-
import numpy as np
import operator
from os import listdir


class KNN(object):
    def classify0(self, inX, dataSet, labels, k):
        dataSetSize = dataSet.shape[0]
        diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
        sqDiffMat = diffMat ** 2
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances ** 0.5
        sortedDistIndicies = distances.argsort()
        classCount = {}
        for i in range(k):
            voteIlabel = labels[sortedDistIndicies[i]]
            classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    def img2vector(self, filename):
        returnVect = np.zeros((1, 1024))
        fr = open(filename)
        for i in range(32):
            lineStr = fr.readline()
            for j in range(32):
                returnVect[0, 32 * i + j] = int(lineStr[j])
        return returnVect

    def handwritingClassTest(self, num):
        hwLabels = []
        trainingFileList = listdir('trainingDigits')  # load the training set
        m = len(trainingFileList)
        trainingMat = np.zeros((m, 1024))
        # 读取所有的训练数据
        for i in range(m):
            fileNameStr = trainingFileList[i]
            fileStr = fileNameStr.split('.')[0]  # take off .txt
            classNumStr = int(fileStr.split('_')[0])
            hwLabels.append(classNumStr)
            trainingMat[i, :] = self.img2vector('trainingDigits/%s' % fileNameStr)
        testFileList = listdir('testDigits')  # iterate through the test set
        fileNameStr = testFileList[num]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = self.img2vector('testDigits/%s' % fileNameStr)
        classifierResult = self.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)

    def testHandwritingClassTest(self, path):
        hwLabels = []
        trainingFileList = listdir('trainingDigits')  # load the training set
        m = len(trainingFileList)
        trainingMat = np.zeros((m, 1024))
        # 读取所有的训练数据
        for i in range(m):
            fileNameStr = trainingFileList[i]
            fileStr = fileNameStr.split('.')[0]  # take off .txt
            classNumStr = int(fileStr.split('_')[0])
            hwLabels.append(classNumStr)
            trainingMat[i, :] = self.img2vector('trainingDigits/%s' % fileNameStr)
        vectorUnderTest = self.img2vector(path)
        classifierResult = self.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d" % classifierResult
