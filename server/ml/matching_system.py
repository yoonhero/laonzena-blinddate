import pandas as pd
import numpy as np
from ml.cosine_similarity import cosine_similarity
from ml.pearson_corr import pearson_similarity


class RecommendSystem():
    def __init__(self, df, csv_path=""):
        self.answers = [["남자", "여자"], ["17살", "18살"], ["INFP", "ENFP", 'ESFJ', "ISFJ", "ISFP", "ESFP", "INTP", "INFJ", "ENFJ", "ENTP", "ESTJ", "ISTJ", "INTJ", "ISTP", "ESTP", "ENTJ"],
                        ["A", "B", "AB", "O"],
                        ["한식", "양식", "중식", "일식"],
                        ["빨강", "주황", "노랑", "초록", "파랑", "보라", "흰색", "검은색"]]

        if csv_path == "":
            self.df = df
        else:
            self.df = pd.read_csv(csv_path)

        self.df = self.df.reset_index(drop=True)

        self.schoolNumber_labels = self.df.iloc[:, 0]
        self.schoolNumber_labels.rename(None, inplace=True)

        self.index_dataframe = self.df.iloc[:, 1:].apply(
            self.get_index, axis=1)

    def get_index(self, df):
        new_row = []

        for idx, answer in enumerate(self.answers):
            no_blank = df[idx].strip()
            try:
                new_row.append(answer.index(no_blank)+1)
            except:
                new_row.append(0)

        return new_row

    def recommend(self, method):
        if method == "cosine":
            print(self.index_dataframe)
            self.result_matrix = np.array([[cosine_similarity(np.array(self.index_dataframe[a]), np.array(
                self.index_dataframe[b])) for a in range(len(self.index_dataframe))] for b in range(len(self.index_dataframe))])

        elif method == "pearson":
            self.result_matrix = np.array([[pearson_similarity(np.array(self.index_dataframe[a]), np.array(
                self.index_dataframe[b])) for a in range(len(self.index_dataframe))] for b in range(len(self.index_dataframe))])

        self.result_dataframe = pd.DataFrame(
            self.result_matrix, columns=self.schoolNumber_labels, index=self.schoolNumber_labels)

        self.clear_center()
        self.result_dataframe.to_csv("result.csv")

    def clear_center(self):
        for i in self.result_dataframe.index:
            self.result_dataframe.loc[i][i] = 0

    def matching(self):
        temp = self.result_dataframe.copy()

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


if __name__ == "__main__":
    recommend = RecommendSystem("./sample_data.csv")

    recommend.recommend("cosine")

    print(recommend.matching())
