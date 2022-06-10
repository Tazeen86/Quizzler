from cProfile import label
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain) -> None:
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label=Label(text="Score 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300, height=250)
        self.canvas_text=self.canvas.create_text(150, 125,width=280, text="Question Goes Here", font=("Ariel", 20, "italic"),fill=THEME_COLOR)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        cross_image = PhotoImage(file="images/false.png")
        
        self.unknown_button = Button(image=cross_image, highlightthickness=0,command=self.false_pressed)
        self.unknown_button.grid(row=2, column=0)

        check_image = PhotoImage(file="images/true.png")
       
        self.known_button = Button(image=check_image, highlightthickness=0,command=self.true_pressed)
        self.known_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white", highlightthickness=0)
        if self.quiz.still_has_questions():
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text,text="No More Questions")
            self.known_button.config(state="disabled")
            self.unknown_button.config(state="disabled")
    def true_pressed(self):
        score,is_right=self.quiz.check_answer("True")
        self.score_label.config(text=f"Score:{score}")
        self.give_feedback(is_right)
        

    def false_pressed(self):
        score,is_right=self.quiz.check_answer("False")
        self.score_label.config(text=f"Score:{score}")
        self.give_feedback(is_right)
        

    def give_feedback(self,is_right):
        if is_right == True:
           self.canvas.config(bg="green", highlightthickness=0)
        else:
            self.canvas.config(bg="red",highlightthickness=0)
        self.window.after(1000, self.get_next_question)

        