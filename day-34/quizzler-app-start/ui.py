from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="Score: 0", font=("Ariel", 10, "italic"), bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvass = Canvas(width=300, height=250)

        self.question_text = self.canvass.create_text(150, 125, width=280,
                                                      text=self.quiz.next_question(),
                                                      fill=THEME_COLOR,
                                                      font=("Ariel", 20, "italic"))
        self.canvass.grid(column=0, row=1, columnspan=2, pady=50)

        btn_wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=btn_wrong_image, highlightthickness=0, command=lambda: self.guess("False"))
        self.wrong_button.grid(column=0, row=2)

        btn_right_image = PhotoImage(file="images/true.png")
        self.btn_right = Button(image=btn_right_image, highlightthickness=0, command=lambda: self.guess("True"))
        self.btn_right.grid(column=1, row=2)

        self.after = ''

        self.window.mainloop()

    def get_next_q(self):
        self.canvass.config(bg="white")
        self.canvass.itemconfigure(self.question_text, text=self.quiz.next_question())

    def guess(self, user_answer):
        result = self.quiz.check_answer(user_answer)
        score = f"{self.quiz.score}/{self.quiz.question_number}"
        self.score.config(text=f"Score: {score}")
        if result:
            print("green")
            self.canvass.config(bg="green")
        else:
            print("red")
            self.canvass.config(bg="red")
        self.get_next_q()
        self.window.after(1000, self.get_next_q())
