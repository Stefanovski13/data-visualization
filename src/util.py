""" Contains helper functions """
import numpy as np
from scipy.spatial.distance import pdist, squareform

csv_relative_path = "../csv/"


def load_csv_to_array(filepath):
    """ Loads csv to numpy matrix """
    return np.genfromtxt(csv_relative_path + filepath, delimiter=',')


def calculate_euclidean_distances(matrix):
    """ Calculates euclidean distances """
    return squareform(pdist(matrix, 'euclidean'))


def reduce_matrix(matrix, k):
    """ Keeps only the k closest points """
    indexes = np.argpartition(matrix, k, axis=1)[:, :k]
    zero_matrix = np.zeros(shape=matrix.shape)
    for i in range(0, matrix.shape[0]):
        zero_matrix[i, indexes[i]] = matrix[i, indexes[i]]

    return zero_matrix
