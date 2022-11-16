import json


class Question():
    def __init__(self):
        self.questions = [
            {"question": "MBTI가 뭔가요?", "answers": ["INFP", "ENFP", 'ESFJ', "ISFJ", "ISFP", "ESFP", "INTP",
                                                   "INFJ", "ENFJ", "ENTP", "ESTJ", "ISTJ", "INTJ", "ISTP", "ESTP", "ENTJ"], "type":"mbti"},
            {"question": "남자인가요? 여자인가요?", "answers": [
                "남자", "여자"], "type":"gender"},
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
