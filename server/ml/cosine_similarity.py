import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm


def cosine_similarity(a, b):
    return np.dot(a, b)/(norm(a) * norm(b))


class CosineSimilarity():
    def __init__(self, dataframe, weight=100):
        self.answers = [["남자", "여자"], ["17살", "18살"], ["INFP", "ENFP", 'ESFJ', "ISFJ", "ISFP", "ESFP", "INTP", "INFJ", "ENFJ", "ENTP", "ESTJ", "ISTJ", "INTJ", "ISTP", "ESTP", "ENTJ"],
                        ["A", "B", "AB", "O"],
                        ["한식", "양식", "중식", "일식"],
                        ["빨강", "주황", "노랑", "초록", "파랑", "보라", "흰색", "검은색"]]

        self.weight = weight

        self.df = dataframe

        self.schoolNumber_labels = self.df.iloc[:, 0]
        self.schoolNumber_labels.rename(None, inplace=True)

        self.index_dataframe = self.df.iloc[:, 1:].apply(
            self.get_index, axis=1)

        self.cosine_similarity_matrix = np.array([[self.cos_sim(np.array(self.index_dataframe[a]), np.array(
            self.index_dataframe[b])) for a in range(len(self.index_dataframe))] for b in range(len(self.index_dataframe))])

        self.cosine_dataframe = pd.DataFrame(self.cosine_similarity_matrix, columns=self.schoolNumber_labels, index=self.schoolNumber_labels)

        for i in self.cosine_dataframe.index:
            self.cosine_dataframe.loc[i][i] = 0

    def get_index(self, df):
        new_row = []
        for idx, answer in enumerate(self.answers):
            no_blank = df[idx].strip()
            weighted_i = answer.index(no_blank) * self.weight / idx
            new_row.append(weighted_i)

        return new_row

    def cos_sim(self, A, B):
        return dot(A, B)/(norm(A)*norm(B))

    def show(self):
        self.cosine_dataframe.head(10)

    def matching(self):
        temp = self.cosine_dataframe.copy()

        self.matching_status = []
        for schoolNumber in self.schoolNumber_labels:
            similairty = temp.loc[schoolNumber, :]

            if similairty.max() == 0:
                continue

            max_similairty_index = similairty.idxmax()

            temp.loc[schoolNumber, :] = 0
            temp.loc[:, schoolNumber] = 0
            temp.loc[max_similairty_index, :] = 0
            temp.loc[:, max_similairty_index] = 0

            self.matching_status.append([schoolNumber, max_similairty_index])

        return self.matching_status
