from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,pady=20,padx=20)
        self.score=Label(text="Score",bg=THEME_COLOR,fg="#FFF",font=("Arial",13,"normal"))
        self.score.grid(column=1,row=0)
        self.canvas=Canvas(width=300,height=250,bg="#fff")
        self.question=self.canvas.create_text(150,125,width=280,text="Hello",font=("Arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2,padx=20,pady=20)

        self.right_logo=PhotoImage(file="Day 32\images\True.png")
        self.true_btn=Button(image=self.right_logo,command=self.true_pressed)   
        self.true_btn.grid(row=2,column=0,pady=20)


        self.wrong_logo=PhotoImage(file="Day 32\images\False.png")
        self.false_btn=Button(image=self.wrong_logo,command=self.false_pressed)
        self.false_btn.grid(row=2,column=1,pady=20)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You've reached the end of the quiz.😊😊")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)