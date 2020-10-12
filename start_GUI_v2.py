from tkinter import *
from functools import partial  # to prevent unwanted windows
import random



class Start:
    def __init__(self, parent):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Set Initial question to zero
        self.starting_amount = IntVar()
        self.starting_amount.set(0)

        # Maths Heading (row 0)
        self.maths_quiz_label = Label(self.start_frame, text="Maths quiz",
                                      font="Arial 19 bold", bg="light green")
        self.maths_quiz_label.grid()

        # initial Instructions (row 1)
        self.maths_instructions = Label(self.start_frame, font="Arial 10 italic",
                                        text="Please enter the amount"
                                             "of questions(between 1 and 30)"
                                             " in the box below. then choose"
                                             "the type of questions you want to do ", wrap=300, justify=LEFT,
                                        padx=10, pady=10)
        self.maths_instructions.grid(row=1, column=0)

        # Entry box... (row 1)
        self.start_quiz_entry = Entry(self.start_frame, font="Arial 19 bold",
                                      width=5)
        self.start_quiz_entry.grid(row=1, column=1)

        # Instructions (row 2)
        self.maths_instructions = Label(self.start_frame, font="Arial 10 italic",
                                        text="Please select the type of questions"
                                             " below to start.")
        self.maths_instructions.grid(row=2, pady=20)

        # Level frame (row 3)
        self.levels_frame = Frame(self.start_frame)
        self.levels_frame.grid(row=3)

        # Buttons goes here...
        level_font = "Arial 12 bold"

        #  Red addition button...
        self.Addition_button = Button(self.levels_frame, text="Addition",
                                      command=lambda: self.to_quiz(1),
                                      font=level_font, bg="Red")
        self.Addition_button.grid(row=0, column=0,padx=20)

        # Orange subtraction button...
        self.subtraction_button = Button(self.levels_frame, text="Subtraction",
                                         command=lambda: self.to_quiz(2),
                                         font=level_font, bg="#FF9933")
        self.subtraction_button.grid(row=0, column=1, padx=20)

        # Yellow multiplication button...
        self.multiplication_button = Button(self.levels_frame, text="multiplication",
                                            command=lambda: self.to_quiz(3),
                                            font=level_font, bg="#FFFF33")
        self.multiplication_button.grid(row=0, column=2, padx=20)

        self.amount_error_label = Label(self.start_frame, text="")
        self.amount_error_label.grid(row=4, pady=20, padx=20)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help", width=10, height=2,
                                  bg="#808080", fg="white", font=level_font)
        self.help_button.grid(row=5, padx=20)

    def to_quiz(self, levels):
        num_questions = self.start_quiz_entry.get()

        # Set error background to white (for testing purposes)...
        self.start_quiz_entry.configure(bg="white")
        self.amount_error_label.config(text="")

        has_error = "no"

        try:
            num_questions = int(num_questions)

            if num_questions < 1 :
                has_error = "yes"
                error_feedback = "Sorry, the minimum question you " \
                                 "can start with is 1"
            elif num_questions > 30:
                has_error = "yes"
                error_feedback = "Sorry, the maximum questions you " \
                                 "can play is 30"

        except ValueError:
            has_error = "yes"
            error_feedback = "Please enter a number (no text / decimals)"

        if has_error == "yes":
            self.start_quiz_entry.config(bg="red")
            self.amount_error_label.config(text=error_feedback)

        else:
            # set number of questions to amount entered by user
            self.starting_amount.set(num_questions)

        def to_quiz(self, levels):

            # retrieve number of questions
            num_questions = self.starting_amount.get()

            Quiz(self, levels, num_questions)

            # Hide start up window
            # Root.withdraw()


class Quiz:
    def __int__(self, partner,  levels, num_questions):
        print(levels)
        print(num_questions)

        # Disable Addition button
        partner.addition_button.config(state=DISABLED)

        # Initialise variable
        self.questions = IntVar()

        # Set number of questions to amount enter by user of the quiz
        self.questions.set(num_questions)

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

        self.question_label = Label(self.questions_frame, text = "? + ? = ")
        self.question_label.grid(row=0, column = 1)


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
