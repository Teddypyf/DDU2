import random
import numpy as np
import matplotlib.pyplot as plt
import math


def generateData(n):
    # generate a random data set in 3*n
    data = []
    i = 0
    while i < (n // 2):
        arr = [random.randint(0, 100), random.randint(0, 100), 1]
        data.append(arr)
        i += 1

    i = 0
    while i < (n // 2):
        arr = [random.randint(0, 100), random.randint(0, 100), 0]
        data.append(arr)
        i += 1

    data = np.asarray(data)
    return data


def plotData(x):
    data = generateData(x)
    redpoint_x = []
    bluepoint_x = []
    redpoint_y = []
    bluepoint_y = []
    for j in range(x):
        x = data[j, 0]
        y = data[j, 1]
        color = data[j, 2]
        if color == 1:
            redpoint_x.append(x)
            redpoint_y.append(y)
        else:
            bluepoint_x.append(x)
            bluepoint_y.append(y)
    bluepoint_x = np.asarray(bluepoint_x)
    bluepoint_y = np.asarray(bluepoint_y)
    redpoint_x = np.asarray(redpoint_x)
    redpoint_y = np.asarray(redpoint_y)

    plt.scatter(bluepoint_x, bluepoint_y)
    plt.scatter(redpoint_x, redpoint_y)
    plt.show()


def one_nn(gendata, x, y):
    data = generateData(gendata)
    dis = 1000000

    redpoint_x = []
    bluepoint_x = []
    redpoint_y = []
    bluepoint_y = []

    for j in range(gendata):
        Inn_x = data[j, 0]
        Inn_y = data[j, 1]
        plotx = data[j, 0]
        ploty = data[j, 1]
        color = data[j, 2]
        Inn_dis = math.sqrt((x - Inn_x) ** 2 + (y - Inn_y) ** 2)
        if Inn_dis < dis:
            dis = Inn_dis
            displyacolor = color

        if color == 1:
            redpoint_x.append(plotx)
            redpoint_y.append(ploty)
        else:
            bluepoint_x.append(plotx)
            bluepoint_y.append(ploty)

    bluepoint_x = np.asarray(bluepoint_x)
    bluepoint_y = np.asarray(bluepoint_y)
    redpoint_x = np.asarray(redpoint_x)
    redpoint_y = np.asarray(redpoint_y)

    plt.scatter(bluepoint_x, bluepoint_y)
    plt.scatter(redpoint_x, redpoint_y)
    plt.scatter(x, y)
    print(displyacolor)
    plt.show()


one_nn(100, 50, 50)
