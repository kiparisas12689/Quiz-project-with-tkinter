from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        self.score_label = Label(text = f"Score: {0}", bg = THEME_COLOR, fg = "white")
        self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(width = 300, height = 250)
        self.canvas.grid(pady = 50, row = 1, column = 0, columnspan = 2)
        self.question_text = self.canvas.create_text(150, 125,
            width = 280,
            text = "Some sort of text",
            font = ("Arial", 20, "italic"),
            fill = THEME_COLOR)

        true = PhotoImage(file = "images/true.png")
        self.green_button = Button(image = true, highlightthickness=0, command = self.true_answer)
        self.green_button.grid(row = 2, column = 0)

        false = PhotoImage(file = "images/false.png")
        self.red_button = Button(image = false, highlightthickness=0, command = self.false_answer)
        self.red_button.grid(row = 2, column = 1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text = f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz.")
            self.green_button.config(state = "disabled")
            self.red_button.config(state = "disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)
