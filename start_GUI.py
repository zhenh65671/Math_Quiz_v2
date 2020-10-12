from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Maths Heading (row 0)
        self.maths_quiz_label = Label(self.start_frame, text="Maths quiz",
                                      font="Arial 19 bold")
        self.maths_quiz_label.grid()

        # initial Instructions (row 1)
        self.maths_instructions = Label(self.start_frame, font="Arial 10 italic",
                                        text="Please enter he amount"
                                             "of questions(between 1 and 30)"
                                             " in the box below. then choose"
                                             "the type of questions you want to do ", wrap=300, justify=LEFT,
                                        padx=10, pady=10)
        self.maths_instructions.grid(row=1, column=0)

        # Entry box... (row 1)
        self.start_quiz_entry = Entry(self.start_frame, font="Arial 16 bold", width=5)
        self.start_quiz_entry.grid(row=1, column=1)

        # Instructions (row 2)
        self.maths_instructions = Label(self.start_frame, font="Arial 10 italic",
                                        text="Please select the type of questions"
                                             " below to start.")
        self.maths_instructions.grid(row=2)

        # button frame (row 3)
        self.quiz_frame = Frame(self.start_frame)
        self.quiz_frame.grid(row=3)

        # Buttons goes here...
        quiz_font = "Arial 12 bold"

        # Red Addition quiz button...
        self.Addition_button = Button(self.quiz_frame, text="Addition",
                                      font=quiz_font, bg="red",
                                      command=lambda: self.to_quiz(1))
        self.Addition_button.grid(row=3,column=0, padx=20)

        #  Orange Subtraction quiz button...
        self.subtraction_button = Button(self.quiz_frame, text="Subtraction",
                                         font=quiz_font, bg="#FF9393",
                                         command=lambda: self.to_quiz(2))
        self.subtraction_button.grid(row=3, column=1, padx=20)
        # Yellow multiplication quiz button...
        self.multiplication_button = Button(self.quiz_frame, text="Multiplication",
                                            font=quiz_font, bg="#FFFF33",
                                            command=lambda: self.to_quiz(3))
        self.multiplication_button.grid(row=3, column=2, padx=20)

    def to_quiz(self, quiz):
        number_of_question = self.start_quiz_entry.get()
        Quiz(self, quiz, number_of_question)


class Quiz:
    def __init__(self, partner, quiz, number_of_question):
        print(quiz)
        print(number_of_question)

        # Disable Addition button
        partner.addition_button.config(state=DISABLED)

        # Initialise variables
        self.n = IntVar()


















# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    something = Start(root)
    root.mainloop()