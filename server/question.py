import json
import torch


class Question():
    questions = {"gender": ["남자", "여자"],
                 "age": ["17살", "18살"],
                 "mbti": ["INFP", "ENFP", 'ESFJ', "ISFJ", "ISFP", "ESFP", "INTP",
                          "INFJ", "ENFJ", "ENTP", "ESTJ", "ISTJ", "INTJ", "ISTP", "ESTP", "ENTJ"],
                 "bloodtype": ["A", "B", "AB", "O"],
                 "favoriteFood": ["한식", "양식", "중식", "일식"],
                 "favoriteColor": [
        "빨강", "주황", "노랑", "초록", "파랑", "보라", "흰색", "검은색"]
    }

    def __init__(self):
        self.questions = [{"question": "남자인가요? 여자인가요?", "answers": [
            "남자", "여자"], "type":"gender"},
            {"question": "몇살인가요?", "answers": ["17살", "18살"], "type":"age"},
            {"question": "MBTI가 뭔가요?", "answers": ["INFP", "ENFP", 'ESFJ', "ISFJ", "ISFP", "ESFP", "INTP",
                                                   "INFJ", "ENFJ", "ENTP", "ESTJ", "ISTJ", "INTJ", "ISTP", "ESTP", "ENTJ"], "type":"mbti"},

            {"question": "혈액형이 무엇인가요?", "answers": [
                "A", "B", "AB", "O"], "type": "bloodtype"},
            {"question": "좋아하는 음식 종류가 무엇인가요?", "answers": [
                "한식", "양식", "중식", "일식"], "type":"favoriteFood"},
            {"question": "좋아하는 색깔이 무엇인가요?", "answers": [
                "빨강", "주황", "노랑", "초록", "파랑", "보라", "흰색", "검은색"], "type":"favoriteColor"},
        ]

    def __getitem__(self, idx):
        return self.questions[idx]

    def get(self, questionNum, answerIdx):
        try:
            temp = self.questions[questionNum]
            return temp.get("answers")[answerIdx], temp.get("type")
        except:
            return None, None

    # Sily One hot Encoding Method
    @staticmethod
    def one_hot_encoding(user):
        schoolNumber, gender, age, mbti, bloodtype, favoriteFood, favoriteColor = user

        q = Question.questions
        gender_zeros = torch.zeros(len(q.get("gender")))
        age_zeros = torch.zeros(len(q.get("age")))
        mbti_zeros = torch.zeros(len(q.get("mbti")))
        bloodtype_zeros = torch.zeros(len(q.get("bloodtype")))
        favoriteFood_zeros = torch.zeros(len(q.get("favoriteFood")))
        favoriteColor_zeros = torch.zeros(len(q.get("favoriteColor")))

        gender_zeros[q.get("gender").index(gender)] = 1
        age_zeros[q.get("age").index(age)] = 1
        mbti_zeros[q.get("mbti").index(mbti)] = 1
        bloodtype_zeros[q.get("bloodtype").index(bloodtype)] = 1
        favoriteFood_zeros[q.get("favoriteFood").index(favoriteFood)] = 1
        favoriteColor_zeros[q.get("favoriteColor").index(favoriteColor)] = 1

        return gender_zeros, age_zeros, mbti_zeros, bloodtype_zeros, favoriteFood_zeros, favoriteColor_zeros


if __name__ == "__main__":
    user = ("10214", "남자", "17살", "ENFJ", "B", "한식", "초록")
    print(Question.one_hot_encoding(user))
