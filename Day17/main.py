from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
  question_text = q["text"]
  question_ans = q["answer"]
  new_question = Question(question_text, question_ans)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
  quiz.next_question()

print("Now you completed your quiz!!")
print(f"Your Final Score is:({quiz.score} / {quiz.question_number}) ")
