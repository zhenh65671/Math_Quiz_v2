from tkinter import *
from functools import partial  # to prevent unwanted windows
import random



class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_quiz)
        self.push_me_button.grid(row=0, pady=10)

    def to_quiz(self):

        # retrieve starting balance
        number_of_questions = 10
        levels = 1

        # Quiz(self, levels, number_of_questions)
        Quiz()

        # hide start up window
        root.withdraw()


class Quiz:
    def __int__(self, partner,  levels, number_of_questions):
        print(levels)
        print(number_of_questions)

        # Disable Addition button
        partner.addition_button.config(state=DISABLED)

        # Initialise variable
        self.questions = IntVar()

        # Set number of questions to amount enter by user of the quiz
        self.questions.set(number_of_questions)

        # GUI setup
        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_box.grid()

        # If use press cross at top, quiz quits
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Heading row
        self.heading_label = Label(self.quiz_frame, text="Heading",
                                   font="Arial 19 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instruction Label
        self.instruction_label = Label(self.quiz_frame, wrap=300, justify=LEFT,
                                       text="Enter your answer in the box "
                                            "below, then press the submit button,"
                                            "to submit your answer.", font="Arial 10 bold",
                                       padx=10, pady=10)
        self.instruction_label.grid(row=1)

        # Question frame
        self.questions_frame = Frame(self.quiz_frame)
        self.questions_frame.grid(row=2, padx=10)

        self.question_label = Label(self.questions_frame, text="? + ? = ")
        self.question_label.grid(row=0, column=1)

        # Answer box
        # self.answer_box = Frame(self.)


        # Answer Label
        self.answer_frame = Frame(self.quiz_frame)
        self.answer_frame.grid(row=1)

        self.score_label = Label(self.quiz_frame, text="score...")
        self.score_label.grid(row=2, column=1)






# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    something = Start(root)
    root.mainloop()
