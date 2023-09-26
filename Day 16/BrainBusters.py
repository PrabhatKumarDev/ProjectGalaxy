from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo
question_bank=[]

# Loop through all the question from question_data and create an object of Question class and append it in question_bank
# Create a list of objects of Question class
for i in range(len(question_data)):
    question=question_data[i]["question"]
    answer=question_data[i]["correct_answer"]
    new_question_obj=Question(question,answer)
    question_bank.append(new_question_obj)

# Create an object of Quiz Brain
quiz=QuizBrain(question_bank)

# Loop run until the question_bank still has question
print(logo)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
