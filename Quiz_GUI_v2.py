from tkinter import *
from functools import partial  # to prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        # GUI to get starting question and level
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_quiz)
        self.push_me_button.grid(row=0, pady=10)

    def to_quiz(self):

        # retrieve starting question
        num_questions = 10
        level = 1

        Quiz(self, level, num_questions)

        # hide start up window
        root.withdraw()

class Quiz:
    def __init__(self, partner, level, num_questions):
        print(level)
        print(num_questions)

        # Initialise variables
        self.question = IntVar()

        # Set num_questions to amount entered by user at the start of the quiz
        self.question.set(num_questions)

        # GUI Setup
        self.quiz_box = Toplevel()

        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Quiz has started"
                                                         " good luck!!",
                                   font="Arial 19 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # question Label
        self.question_frame = Frame(self.quiz_frame)
        self.question_frame.grid(row=1)

        # Question frame
        self.questions_frame = Frame(self.quiz_frame)
        self.questions_frame.grid(row=2, padx=10)

        self.questions_label = Label(self.questions_frame, text="? + ? = ",
                                     font="Arial 16 bold", bg="#58D3F7")
        self.questions_label.grid(row=0, column=0)

        # Answer box
        self.answer_entry = Label(self.questions_frame, font="Arial 19 bold", width=5)
        self.answer_entry.grid(row=0, column=1)

        # Next button
        self.next_button = Button(self.questions_frame, text="NEXT",
                                  font="Arial 16 bold", bg="#808080", fg="white")
        self.next_button.grid(row=0, column=2, padx=20)







# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box quiz")
    something = Start(root)
    root.mainloop()