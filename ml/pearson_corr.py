# Matching Algorithm with Pearson Correlation

import numpy as np
from scipy.stats import pearsonr
import pandas as pd


def pearsonR(s1, s2):
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()

    return np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2)*np.sum(s2_c**2))


def recommend():
    return


def pearson_similarity(a, b):
    return np.dot((a-np.mean(a)), (b-np.mean(b))) / ((np.linalg.norm(a-np.mean(a))) * (np.linalg.norm(b-np.mean(b))))


if __name__ == '__main__':
    user_a = [5.0, 0.5, 5.0, 4.5, 3.5]
    user_b = [5.0, 3.0, 5.0, 5.0, 5.0]

    print(pearson_similarity(user_a, user_b))

    print(pearsonr(user_a, user_b)[0])

    # df.corr(method="pearson")