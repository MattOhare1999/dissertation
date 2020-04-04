import os

import numpy as np
from scipy.spatial import distance

variance = []
user_ids = []


def load_file(name, dtype):
    """
    load in the file, get user ids and variance of each column
    """
    with open(f'datasets/{name}', encoding='utf8') as data_file:

        ncols = len(data_file.readline().split(','))
        global user_ids
        user_ids = get_user_ids(data_file)
        data_file.close()

    with open(f'datasets/{name}', encoding='utf8') as data_file:

        file = np.loadtxt(data_file,
                          skiprows=1,
                          usecols=range(1, ncols),
                          delimiter=',',
                          dtype=dtype,
                          comments='#')
        variance.append(np.var(file, 0, ddof=1))
        for j in range(len(variance[0])):
            if variance[0][j] == 0:
                variance[0][j] = 1
        return file


def load_ids(name, dtype):
    """
    load in the user ids 
    """
    with open(f'datasets/{name}', encoding='utf8') as data_file:
        user_ids = get_user_ids(data_file)
        return user_ids


def get_user_ids(data_file):
    """
    return list of user ids
    """
    user_list = []
    for line in data_file:
        user_list.append(line.split(',')[0])
    return user_list


def load_id(apps, size):
    """
    load in the user ids of the specified dataset
    """
    return load_ids(f'app_usage/top_{apps}_apps/top{apps}_app_usage{size}.csv',
                    np.int16)


def load_app_usage(apps, size):
    """
    load in the specified dataset 
    """
    return load_file(
        f'app_usage/top_{apps}_apps/top{apps}_app_usage{size}.csv', np.int16)


def get_variance():
    """
    return the variance of the data 
    """
    return variance


def grouped(iterable, n):
    return zip(*[iter(iterable)] * n)


def annotate_app_usage(node, i):
    """
    return user id to allow layout to be annotated 
    """
    global user_ids
    user_id = "User Id: " + str(user_ids[i])
    return user_id


def app_usage_distance(h1, h2):
    """
    similarity metric between two users 
    """
    """ hamming distance """
    # return distance.hamming(h1, h2)
    """ euclidean distance """
    #return np.linalg.norm(h2 - h1)
    """ standardised euclidean distance """
    return distance.seuclidean(h1, h2, variance)
