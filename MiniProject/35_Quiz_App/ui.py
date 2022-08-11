from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Super Quiz")
        self.window.config(bg=THEME_COLOR, highlightthickness=0, padx=20, pady=20)

        self.right_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")

        self.points = 0
        self.score = Label(
            text=f"Score: {self.points}",
            bg=THEME_COLOR,
            fg="white",
            padx=20,
            pady=20,
            font=("Ariel", 16, "italic")
        )
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_next_question()

        self.right = Button(image=self.right_img, padx=20, pady=20, command=self.right_option)
        self.right.grid(row=2, column=0)

        self.wrong = Button(image=self.wrong_img, padx=20, pady=20, command=self.left_option)
        self.wrong.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of the Quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def show_results(self, answer):
        result = self.quiz.check_answer(answer)
        self.give_feedback(result)

    def right_option(self):
        self.show_results("true")

    def left_option(self):
        self.show_results("false")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

