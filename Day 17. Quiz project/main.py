from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_list = []
for question in question_data:
    question_list.append(Question(question["text"], question["answer"]))
quiz = QuizBrain(question_list)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz.\nYour final score "
      f"is: {quiz.score}/{quiz.question_number}.")