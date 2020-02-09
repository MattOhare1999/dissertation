import numpy as np
import os
from scipy.spatial import distance

variance = []
global user_ids


def load_file(name, dtype):
    with open(f'datasets/{name}', encoding='utf8') as data_file:

        ncols = len(data_file.readline().split(','))
        # remove /n string replace ('/n) ,''
        global user_ids
        user_ids = get_user_ids(data_file)
        # user_ids.append(data_file.readline().split(',')[0])
        data_file.close()

    with open(f'datasets/{name}', encoding='utf8') as data_file:

        file = np.loadtxt(data_file,
                          skiprows=1,
                          usecols=range(1, ncols),
                          delimiter=',',
                          dtype=dtype,
                          comments='#')
        variance.append(np.var(file, 0))
        return file


def load_ids(name, dtype):
    with open(f'datasets/{name}', encoding='utf8') as data_file:
        user_ids = get_user_ids(data_file)
        return user_ids


def get_user_ids(data_file):
    user_list = []
    for line in data_file:
        user_list.append(line.split(',')[0])
    return user_list


def load_id(apps, size):
    return load_ids(f'app_usage/top{apps}_app_usage{size}.csv', np.int16)


def get_variance():
    return variance


def load_app_usage(apps, size):
    return load_file(f'app_usage/top{apps}_app_usage{size}.csv', np.int16)


def grouped(iterable, n):
    return zip(*[iter(iterable)] * n)


def annotate_app_usage(node, i):
    global user_ids
    user_id = "User Id: " + str(user_ids[i])
    return user_id


def app_usage_distance(h1, h2):
    """
    similarity metric between two users hands
    """
    """ hamming distance """
    #return distance.hamming(h1, h2)
    """ euclidean distance """
    return np.linalg.norm(h2 - h1)
    """ standardised euclidean distance """
    # return distance.seuclidean(h1, h2, variance)
