from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question = Question(q["text"], q["answer"])
    question_bank.append(question)
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print(f"Your score is {quiz_brain.score}")







