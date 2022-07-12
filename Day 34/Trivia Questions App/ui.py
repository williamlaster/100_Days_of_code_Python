from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizGUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=275, text="", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(
            image=false_img, highlightthickness=0, command=self.answer_false)
        self.false.grid(row=2, column=0)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(
            image=true_img, highlightthickness=0, command=self.answer_true)
        self.true.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}"
            )
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.user_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.user_feedback(is_right)

    def user_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_question)
