from day_17_data import question_data
from day_17_question_model import Question
from day_17_quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

    # print(f"Question: {question_text},\nAnswer: {question_answer}")
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

# item = (Question.[i]['text'], Question.[i]['answer'])
# question_bank += item

print("You've complete the challenge")
print(f"Your total score is {quiz.score}/{len(question_bank)}")



# print(question_data[4]['text'])
