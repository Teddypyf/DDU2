import csv
import random
import numpy as np
import matplotlib.pyplot as plt
import math


def read_csv_file(file_path):
    data = []
    with open(file_path, "r", newline="", encoding="utf-8-sig") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=";")
        for row in csv_reader:
            # 将每一行的除了最后一列的数据放入一个数组中，并将数据转换为浮点数
            data_row = [float(value) for value in row[:-1]]
            data_row.append(row[-1])  # 将最后一个元素作为单独的元素加入数组
            data.append(data_row)
    return data


def distance(file_path, x, y, z):
    dis_array = []
    dis_data = np.array(read_csv_file(file_path))
    array_length = len(read_csv_file(file_path))
    for row in range(array_length):
        row_distance = []
        print(dis_data[row, :-1])
        distance = np.abs(dis_data[row, :-1] - np.array([x, y, z]))
        row_distance.append(distance)
        row_distance.append(data[row, -1])
        dis_array.append([row_distance])
    return dis_array


print(distance("KNN_alg\knntraindata.csv", 1, 1, 1))
