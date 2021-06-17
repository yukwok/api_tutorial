from tkinter import *
from PIL import ImageTk, Image


THEME_COLOR = "#375362"
PATH1 = "./images/false.png"
PATH2 = "./images/true.png"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="some question text",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.false_button_img = ImageTk.PhotoImage(Image.open(PATH1))
        self.false_button = Button(image=self.false_button_img, highlightthickness=0)
        self.false_button.grid(column=0, row=2)

        self.true_button_img = ImageTk.PhotoImage(Image.open(PATH2))
        self.true_button = Button(image=self.true_button_img, highlightthickness=0)
        self.true_button.grid(column=1, row=2)

        self.window.mainloop()
