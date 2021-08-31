import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInteface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=2, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, text='question', font=('Ariel', 20, "italic"))

        self.true_button_img = tkinter.PhotoImage(file='./images/true.png')
        self.false_button_img = tkinter.PhotoImage(file="./images/false.png")
        self.true_button = tkinter.Button(image=self.true_button_img, text='True', command=self.true_click)
        self.true_button.grid(column=0, row=4)
        self.false_button = tkinter.Button(image=self.false_button_img, text='False', command=self.false_click)
        self.false_button.grid(column=1, row=4)
        self.scoreboard_label = tkinter.Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR)
        self.scoreboard_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.scoreboard_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You`ve reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_click(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
