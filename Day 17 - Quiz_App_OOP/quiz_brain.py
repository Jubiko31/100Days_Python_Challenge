from data import descriptions

class QuizBrain:
    is_over = False
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    
    def questions_is_over(self):
        return self.question_number < len(self.question_list)     
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        if self.question_list == 25:
            input(f"Q.{self.question_number} Winter is here: {current_question.text}")
        user_answer = input(f"Q.{self.question_number}:  {current_question.text} ({descriptions[self.question_number - 1]})\n")
        
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it!\n')
        else:
            self.is_over = True            
        