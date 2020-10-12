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
                                  font="Arial 16 bold", bg="#33FFF3", fg="white")
        self.next_button.grid(row=0, column=2, padx=20)

        # Score Label
        start_text = "Score:{}".format(correct_question/total_questions)
        total_questions = self.num_questions.get()

        self.balance_label = Label(self.questions_frame, font="Arial 19 bold", fg="green",
                                   text=start_text, wrap=288,
                                   justify=LEFT)
        self.balance_label.grid(row=1, column=0, pady=10, padx=10)

        # Submit button
        self.submit_button = Button(self.questions_frame, text="Submit",
                                    font="Arial 16 bold", bg="#6AFF33", fg="white")
        self.submit_button.grid(row=1, column=1, pady=20)

        # Help and quiz stats button (row 3)
        self.help_export_frame = Frame(self.quiz_frame)
        self.help_export_frame.grid(row=4, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white")
        self.help_button.grid(row=4, column=0, padx=20)

        self.stats_button = Button(self.help_export_frame, text="quiz Stats",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=4, column=1, padx=20)

        # Quit Button
        self.quit_button = Button(self.quiz_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=20)
        self.quit_button.grid(row=5, pady=10)

    def to_quit(self):
        root.destroy()







# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box quiz")
    something = Start(root)
    root.mainloop()