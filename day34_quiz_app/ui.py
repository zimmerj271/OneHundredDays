from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score label
        self.score_label = Label(font=("Arial", 12), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas to add text
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some Question Here",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        # self.question_text = self.canvas.create_text(text="Some Question Text")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.check_true)
        self.true_button.grid(column=0, row=2, pady=20)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.check_false)
        self.false_button.grid(column=1, row=2, pady=20)
        self.next_question()

        # while loop to keep window on the screen
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()

            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text,
                                      text=f"Final Score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        check_answer = self.quiz.check_answer("True")
        self.give_feedback(check_answer)

    def check_false(self):
        check_answer = self.quiz.check_answer("False")
        self.give_feedback(check_answer)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

