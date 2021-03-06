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

        # Enter button (row 2)
        self.Enter_button = Button(self.start_frame, text="Enter", font="Arial 16 bold",
                                   bg="#D0CEE2", width=5, command=self.check_question)
        self.Enter_button.grid(row=2, column=1, padx=10)

        # Level frame (row 3)
        self.levels_frame = Frame(self.start_frame)
        self.levels_frame.grid(row=3)

        # Buttons goes here...
        level_font = "Arial 12 bold"

        #  Red addition button...
        self.Addition_button = Button(self.levels_frame, text="Addition",
                                      command=lambda: self.to_quiz(1),
                                      font=level_font, bg="Red")
        self.Addition_button.grid(row=0, column=0, padx=20)

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

        self.Addition_button.config(state=DISABLED)
        self.subtraction_button.config(state=DISABLED)
        self.multiplication_button.config(state=DISABLED)

        self.amount_error_label = Label(self.start_frame, text="")
        self.amount_error_label.grid(row=4, pady=20, padx=20)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help", width=10, height=2,
                                  bg="#808080", fg="white", font=level_font,
                                  command=self.to_help)
        self.help_button.grid(row=5, padx=20)

    def check_question(self):
        num_questions = self.start_quiz_entry.get()

        # Set error background to white (for testing purposes)...
        self.start_quiz_entry.configure(bg="white")
        self.amount_error_label.config(text="")

        has_error = "no"

        try:
            num_questions = int(num_questions)

            if num_questions < 1:
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
            self.Addition_button.config(state=DISABLED)
            self.subtraction_button.config(state=DISABLED)
            self.multiplication_button.config(state=DISABLED)

        else:
            # set number of questions to amount entered by user
            self.starting_amount.set(num_questions)

        # retrieve number of questions
        num_questions = self.starting_amount.get()

        if has_error == "no":
            self.Addition_button.config(state=NORMAL)
            self.subtraction_button.config(state=NORMAL)
            self.multiplication_button.config(state=NORMAL)

    def to_quiz(self, levels):
        num_questions = self.starting_amount.get()

        # self.start_frame.destroy()
        self.start_frame.destroy()
        Quiz(self, levels, num_questions)

        # Hide start up window
        # Root.withdraw()

    def to_help(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.config()


class Quiz:
    def __init__(self, partner, levels, how_many):
        print(levels)
        print(how_many)
        self.quiz_round_result = [how_many, 0]
        self.round_results_list = []

        # Initialise variables
        # set number of questions to be asked
        self.num_questions = IntVar()
        self.num_questions.set(how_many)

        self.num_answered = IntVar()
        self.num_answered.set(0)

        self.num_correct = IntVar()
        self.num_correct.set(0)

        self.correct = IntVar()
        self.correct.set(0)
        self.correct.get()

        self.op_level = IntVar()
        self.op_level.set(levels)

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

        # Questions frame
        self.questions_frame = Frame(self.quiz_frame)
        self.questions_frame.grid(row=2, padx=10)

        self.questions_label = Label(self.questions_frame, text="? + ? = ",
                                     font="Arial 16 bold", bg="#58D3F7")
        self.questions_label.grid(row=0, column=0)

        # Answer box
        self.gk_ans = Entry(self.questions_frame, font="Arial 19 bold", width=5)
        self.gk_ans.grid(row=0, column=1)

        # Next button
        self.next_button = Button(self.questions_frame, text="NEXT",
                                  font="Arial 16 bold", bg="#33FFF3", fg="white",
                                  command=self.next_question)
        self.next_button.grid(row=0, column=2, padx=20)

        # Score Label
        self.score_label = Label(self.questions_frame, font="Arial 19 bold", fg="green",
                                    wrap=288,
                                   justify=LEFT)
        self.score_label.grid(row=1, column=0, pady=10, padx=10)

        # Submit button
        self.submit_button = Button(self.questions_frame, text="Submit",
                                    font="Arial 16 bold", bg="#6AFF33", fg="white",
                                    command= self.check_answer)
        self.submit_button.grid(row=1, column=1, pady=20)

        self.answer_error_label = Label(self.questions_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275)
        self.answer_error_label.grid(row=2, columnspan=2, pady=5)

        # Help and quiz stats button (row 3)
        self.help_export_frame = Frame(self.quiz_frame)
        self.help_export_frame.grid(row=4, pady=10)

        self.stats_button = Button(self.help_export_frame, text="quiz Stats",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=4, column=1, padx=20)

        # Quit Button
        self.quit_button = Button(self.help_export_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=10,
                                  command=self.to_quit)
        self.quit_button.grid(row=4, column=0, padx=20)

    def check_answer(self):
        # set the background colour of the entry box
        self.gk_ans.config(bg="#ffffff")

        num_questions = self.num_questions.get()
        num_correct = self.num_correct.get()

        # Get the amount of questions enter by user
        num_complete = self.num_answered.get()

        # disable next button until user submit their answer
        self.next_button.config(state=DISABLED)
        self.submit_button.config(state=DISABLED)

        # Set error background colour (and assume that there are no
        # errors at the start
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes) ...
        self.gk_ans.config(bg="white")
        self.gk_ans.config(text="")

        var_correct = self.correct.get()

        # Get the answer enter by user
        gk_ans = self.gk_ans.get()
        print("GK ans", gk_ans)

        try:
            correct = int(var_correct)
            gk_ans = int(gk_ans)
            self.quiz_round_result.append(gk_ans)

            if gk_ans != correct:
                self.answer_error_label.config(text="oops the answer you enter is incorrect")
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)
                round_results = "{} / {}".format(num_correct, num_questions)
                num_complete += 1
                num_correct = num_correct
                self.round_results_list.append(round_results)

            elif gk_ans == correct:
                self.answer_error_label.config(text="Well done", fg="green")
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)

                round_results = "Score {} / {}".format(num_correct, num_questions)
                num_correct += 1
                num_complete += 1
                # self.score_label.config(text="{} / {}".format(num_correct, num_complete))
                self.round_results_list.append(round_results)
                self.quiz_round_result[1] = correct

            self.score_label.config(text="{} / {}".format(num_correct, num_complete))
            self.correct.set(var_correct)
            self.num_correct.set(num_correct)
            self.num_answered.set(num_complete)

        except ValueError:
            has_errors = "yes"
            self.answer_error_label = Label(self.questions_frame, text="Please enter you answer",
                                            font="Arial 10 bold", fg="black", bg="cyan", pady=10, width=20)
            self.answer_error_label.grid(row=3, column=1)

    def next_question(self):
        how_many = self.num_answered.get()
        max_questions = self.num_questions.get()

        if how_many == max_questions:
            self.next_button.config(state=DISABLED)
            self.submit_button.config(state=DISABLED)

            # When user finish the amount of question they set quiz finish
            self.answer_error_label.config(text="Quiz Over - you have answered all the questions, "
                                                "click Stats button to review.")

        level = self.op_level.get()

        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)

        question = ""

        # Disable next button at start
        self.next_button.config(state=DISABLED)

        # After user generated the question enable the submit button
        self.submit_button.config(state=NORMAL)

        # After user push the next button, delete the answer from the last question
        self.gk_ans.delete(0, 'end')

        if level == 1:
            operator = "+"
            question = "{} {} {}".format(num1, operator, num2)

        elif level == 2:
            operator = "-"
            question = "{} {} {}".format(num1, operator, num2)

            if num2 > num1:
                num1, num2 = num2, num1

        if level == 3:
            num1 = random.randint(1, 15)
            num2 = random.randint(1, 15)
            operator = "*"

            # setting the format for the question
            question = "{} {} {}".format(num1, operator, num2)
            display_question = "{} * {} = ".format(num1, num2)

        else:
            display_question = "{} =".format(question)
            self.num_answered.set(how_many)

        self.questions_label.config(text=display_question)


        answer = eval(question)
        self.correct.set(answer)

        print("answer", answer)
        print("{} {}".format(display_question, answer))

        self.correct.set(answer)


    def to_quit(self):
        root.destroy()


class Help:
    def __init__(self, partner):
        background = "grey"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window  (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "Choose an amount to play with and then choose the level.  " \
                    "It have three different levels, addition, subtraction" \
                    "and multiplication \n\n" \
                    "When you enter the play area, you will see the question " \
                    "and a box next to it. Than you can push the submit you answer," \
                    "after you checked your answer you can go to the next question." \
                    "If your answer is right the background will be green otherwise is will be red." \
                    "\n\n \"" \

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, pady=10, padx=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="#660000", font="arial 15 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths quiz")
    something = Start(root)
    root.mainloop()
