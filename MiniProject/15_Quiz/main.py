from data import *
from question_model import *
from quiz_brain import *

question_bank = []
for n in question_data:
    obj = Question(n["text"], n["answer"])
    question_bank.append(obj)

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
