from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, qb: QuizBrain):
        self.quiz = qb
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125, width=280, text="Some Question text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        t_img = PhotoImage(file="images/true.png")
        f_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=t_img, highlightthickness=0, command=self.left_clicked)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(image=f_img, highlightthickness=0, command=self.right_clicked)
        self.false_btn.grid(row=2, column=1)
        self.get_next_question()      
               
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():    
            self.score_label.config(text=f"Score: {self.quiz.score}")
            next_q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_q)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You made it! Score: {self.quiz.score}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
        
    def right_clicked(self):
        is_correct = self.quiz.check_answer("False")
        self.feedback(is_correct)

    def left_clicked(self):
        is_correct = self.quiz.check_answer("True")
        self.feedback(is_correct)
        
    def feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
