# Classic Quiz game: Game of Thrones edition
import random
from question_model import Question
from quiz_brain import QuizBrain
from data import questions, fatalities, logo

print(logo)
print("When you play Game of Thrones quiz, you win or you die, there is no middleground.")
print("25 Questions quiz which will test true ASoIaF fan.\nEach question is next level, you lose you die, so get ready, Winter is coming...")

questions_list = []

for question in questions:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    
    questions_list.append(new_question)

quiz = QuizBrain(questions_list)

def main():
    while quiz.questions_is_over():
        quiz.next_question()
        if quiz.is_over:
            print('Wrong\n')
            lose = random.choice(fatalities)
            print(lose)
            return
    
    print('Congrats. You are worthy to play the Game of Thrones')
    
main()
