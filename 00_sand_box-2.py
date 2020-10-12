from tkinter import *
from functools import partial
import random
import tkinter as tk


class Start:
    def __init__(self, parent):

        # Frame for the titles as well as the instructions
        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        # Frame for the help button
        self.help_frame = Frame(pady=10, padx=10)
        self.help_frame.grid()

        # setting the number of questions as an interger and zero
        self.number_questions = IntVar()
        self.number_questions.set(0)

        # setting the low number as an interger and zero
        self.numbers_used_low = IntVar()
        self.numbers_used_low.set(0)

        # setting the high number as an interger and zero
        self.numbers_used_high = IntVar()
        self.numbers_used_high.set(0)

        # setting the number of questions as an interger and zero
        self.question_amount = IntVar()
        self.question_amount.set(0)

        # Label for the main title
        self.math_quiz_label = Label(self.start_frame,
                                          text="Math Quiz",
                                          font=("Arial", "19", "bold"),
                                          padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

        # label for the instructions for the start of the quiz
        self.math_instructions = Label(self.start_frame, font="Arial 10 italic",
                                       text="Please enter the number of "
                                            "questions you would like to "
                                            "answer in the box below. Keep "
                                            "in mind that you cant have less "
                                            "than 0 questions!",
                                            wrap=275, justify=LEFT,
                                            padx=10, pady=10,)
        self.math_instructions.grid(row=1)

        # frame for the entry boxes labels
        self.question_frame = Frame(self.start_frame, width=10)
        self.question_frame.grid(row=2)

        # frame for the entry boxes
        self.entry_frame = Frame(self.start_frame, width=5)
        self.entry_frame.grid(row=3)

        # label for the amount of questions
        self.add_questions_button = Label(self.question_frame,
                                       font="Arial 15 bold",
                                       text="Set Amount of Questions")
        self.add_questions_button.grid(row=0, column=0)

        # entry box for amount of questions
        self.start_amount_entry = Entry(self.question_frame,
                                        font="Arial 19 bold", width=10,)
        self.start_amount_entry.grid(row=0, column=1)

        # label for displaying the errors
        self.amount_error_label = Label(self.question_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # label for numbers low and numbers high
        self.numbers_between_button = Label(self.entry_frame,
                                       font="Arial 15 bold",
                                       text="Use numbers between")
        self.numbers_between_button.grid(row=2, column=0)

        # Low number entry box
        self.numbers_used_entry_low = Entry(self.entry_frame,
                                        font="Arial 19 bold", width=5)
        self.numbers_used_entry_low.grid(row=2, column=1, padx=20)

        # label for text between to 2 entry boxes
        self.numbers_between_button = Label(self.entry_frame,
                                       font="Arial 15 bold",
                                       text="and")
        self.numbers_between_button.grid(row=2, column=2)

        # high number entry box
        self.numbers_used_entry_high = Entry(self.entry_frame,
                                        font="Arial 19 bold", width=5)
        self.numbers_used_entry_high.grid(row=2, column=3, padx=20)

        # low number entry box
        self.numbers_error_label = Label(self.question_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275, justify=LEFT)
        self.numbers_error_label.grid(row=3, columnspan=2, pady=5)

        # button frame (row 4)
        self.question_type_frame = Frame(self.start_frame)
        self.question_type_frame.grid(row=4)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Blue Multiplication question_type button
        self.multiplication_button = Button(self.question_type_frame, text="Multiplication",
                                       command=lambda: self.to_quiz("*"),
                                       font=button_font, bg="#1170ed")
        self.multiplication_button.grid(row=0, column=0, pady=10)

        # Yellow Subtraction question_type button
        self.subtraction_button = Button(self.question_type_frame, text="Subtraction",
                                       command=lambda: self.to_quiz("-"),
                                       font=button_font, bg="#FFFF33")
        self.subtraction_button.grid(row=0, column=1, pady=10)

        # Green Addition question_type button
        self.addition_button = Button(self.question_type_frame, text="Addition",
                                       command=lambda: self.to_quiz("+"),
                                       font=button_font, bg="#99FF33")
        self.addition_button.grid(row=0, column=2, pady=10)

        # help button
        self.help_button = Button(self.help_frame, text="How to Play",
                                       font=button_font, bg="#808080", fg="white",
                                       command=self.to_help)
        self.help_button.grid(row=1, column=1, pady=10)

    def to_quiz(self, question_type):
        # Number checking function
        question_amount = self.start_amount_entry.get()

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        try:
            question_amount = int(question_amount)

            if question_amount <= 0:
                has_errors = "yes"
                error_feedback = "Sorry, the smallest amount of " \
                                 "questions you can play with is 1"
            elif question_amount > 50:
                has_errors = "yes"
                error_feedback = "You cannot play with more than 50 " \
                                 "Questions!"

            elif question_amount >= 1:
                self.number_questions.set(question_amount)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number(no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:

            numbers_used_low = self.numbers_used_entry_low.get()

            error_back = "#ffafaf"
            has_errors = "no"

            self.start_amount_entry.config(bg="white")
            self.amount_error_label.config(text="")

            try:
                numbers_used_low = int(numbers_used_low)

                if numbers_used_low <= 0:
                    has_errors = "yes"
                    error_feedback = "Sorry, the smallest number you " \
                                     "can play with is 1"
                elif numbers_used_low > 50:
                    has_errors = "yes"
                    error_feedback = "You cannot play with numbers " \
                                     "over 50!"

                elif numbers_used_low >= 1:
                    self.numbers_used_low.set(numbers_used_low)

            except ValueError:
                has_errors = "yes"
                error_feedback = "Please enter a whole number(no text / decimals)"

            if has_errors == "yes":
                self.start_amount_entry.config(bg=error_back)
                self.amount_error_label.config(text=error_feedback)

            else:

                numbers_used_high = self.numbers_used_entry_high.get()

                error_back = "#ffafaf"
                has_errors = "no"

                self.start_amount_entry.config(bg="white")
                self.amount_error_label.config(text="")

                try:
                    numbers_used_high = int(numbers_used_high)

                    if numbers_used_high <= 0:
                        has_errors = "yes"
                        error_feedback = "Sorry, the smallest amount of " \
                                         "questions you can play with is 1"
                    elif numbers_used_high > 50:
                        has_errors = "yes"
                        error_feedback = "You cannot use numbers over 50! "

                    elif numbers_used_high >= 1:
                        self.numbers_used_high.set(numbers_used_high)

                    elif numbers_used_high <= numbers_used_low:
                        has_errors = "yes"
                        error_feedback = " Your right hand number cannot be " \
                                         "larger than your left hand number!"

                except ValueError:
                    has_errors = "yes"
                    error_feedback = "Please enter a whole number(no text / decimals)"

                if has_errors == "yes":
                    self.start_amount_entry.config(bg=error_back)
                    self.amount_error_label.config(text=error_feedback)

                else:

                    # code for starting game:
                    self.number_questions.set(question_amount)

                    question_amount = self.number_questions.get()
                    numbers_used_low = self.numbers_used_low.get()
                    numbers_used_high = self.numbers_used_high.get()

                    Quiz(self, question_type, question_amount, numbers_used_low, numbers_used_high)

                    # hide start up menu
                    root.withdraw()

    def to_help(self):
        get_help = Help(self)


class Quiz:
    def __init__(self, partner, question_type, question_amount, numbers_used_low,
                 numbers_used_high):

        self.quiz_results_list = [question_amount, 0]
        self.round_results_list = []

        # importing numbers inputed by the user for generating questions
        self.var_low = IntVar()
        self.var_low.set(numbers_used_low)

        self.var_high = IntVar()
        self.var_high.set(numbers_used_high)

        # importing numbers inputed by the user for generating questions
        self.var_question_number = IntVar()
        self.var_question_number.set(question_amount)

        # importing question inputed by the user for generating questions
        self.var_question = StringVar()
        self.var_question.set('')

        # setting the score as an interger
        self.score = IntVar()

        # Importing the correct answer
        self.var_correct_ans = IntVar()
        self.var_correct_ans.set(0)

        # Importing the correct answer
        self.var_ques_number = IntVar()
        self.var_ques_number.set(1)

        # Importing the type of question
        self.var_operation = StringVar()
        self.var_operation.set(question_type)

        # GUI Setup
        self.quiz_box = Toplevel()

        # So user can quit with x in top corner
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        # Frame for main quiz functions
        self.quiz_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.quiz_frame.grid()

        # Frame for help button
        self.help_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.help_frame.grid()

        # Frame for the quit button
        self.quit_frame = Frame(self.quiz_box, pady=10, padx=10)
        self.quit_frame.grid()

        # Top heading
        self.math_quiz_label = Label(self.quiz_frame,
                                          text="Play",
                                          font=("Arial", "19", "bold"),
                                          padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

        # Instructions for user
        self.math_instructions = Label(self.quiz_frame, font="Arial 10 italic",
                                       text="Click on the Next button "
                                            "to continue. Then click on "
                                            "the submit button to check you're "
                                            "answer.  ",
                                            wrap=275, justify=LEFT,
                                            padx=10, pady=10,)
        self.math_instructions.grid(row=1)

        # question number
        self.question_number_label = Label(self.quiz_frame,
                                          text="Question 1",
                                          font=("Arial", "12", "bold"),
                                          padx=10, pady=10)
        self.question_number_label.grid(row=2)

        # used to display the questions
        self.questions_label = Label(self.quiz_frame,
                                       font="Arial 15 bold",
                                       text="")
        self.questions_label.grid(row=4, column=0)

        # entry box for answers
        self.question_answer_entry = Entry(self.quiz_frame, text="",
                                        font="Arial 19 bold", width=5)
        self.question_answer_entry.grid(row=4, column=1, padx=15)

        # space where the errors are displayed
        self.amount_error_label = Label(self.quiz_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=3, columnspan=2, pady=5)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Submit answer button
        self.submit_button = Button(self.quiz_frame, text="Submit",
                                            command=lambda: self.check_answer(question_amount),
                                            font=button_font, bg="#4ee6ab")
        self.submit_button.grid(row=5, column=1, pady=10)

        # next question button
        self.next_button = Button(self.quiz_frame, text="Next",
                                            command=lambda: self.next_question(question_amount),
                                            font=button_font, bg="#4ee6ab")
        self.next_button.grid(row=5, column=0, pady=10)

        # help button
        self.help_button = Button(self.help_frame, text="How to Play",
                                       bg="#808080", fg="white",
                                       font="Arial 15 bold",
                                       command=self.to_help)
        self.help_button.grid(row=1, column=0, pady=5)

        # help button
        self.stats_btn = Button(self.help_frame, text="Quiz Results...",
                                   font="Arial 15 bold",
                                   command=lambda: self.to_stats(self.round_results_list, self.quiz_results_list),
                                   bg="#003366", fg="white")
        self.stats_btn.grid(row=1, column=1, pady=5)

        # Quit button
        self.quit_button = Button(self.quit_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold",
                                  command=self.to_quit, padx=10, pady=5)
        self.quit_button.grid(row=7, pady=10, column=1)

        # ensuring the user cannot click submit with no question
        self.submit_button.config(state=DISABLED)

    def next_question(self, question_amount):
        # color for when box is cleared (white)
        box_clear = "#ffffff"

        self.question_answer_entry.config(bg=box_clear)
        self.question_answer_entry.delete(0, 'end')

        self.next_button.config(state=DISABLED)
        var_new_question_num = self.var_ques_number.get()

        question_num_text = "Question {}".format(var_new_question_num)
        self.question_number_label.config(text=question_num_text)

        # reactivating the submit answer button
        self.submit_button.config(state=NORMAL)

        low_num = self.var_low.get()
        high_num = self.var_high.get()

        num_1 = random.randint(low_num, high_num)
        num_2 = random.randint(low_num, high_num)

        # add one to question number and set the variable
        var_new_question_num += 1
        self.var_ques_number.set(var_new_question_num)

        # getting the type of question
        operator = self.var_operation.get()

        # if the operator is * set it as a more recognisable symbol(×)
        if operator == "*":
            display_op = "×"
        else:
            display_op = operator

        # setting the layout for the question
        question = "{} {} {}".format(num_1, operator, num_2)

        # creating a question that has the more recognisable symbol
        display_question = "{} {} {} = ".format(num_1, display_op, num_2)
        self.questions_label.config(text=display_question)

        # setting the correct answer and the display question as variables to carry over to the rest of the quiz
        answer = eval(question)
        self.var_correct_ans.set(answer)
        self.var_question.set(display_question)

    def check_answer(self, question_amount):

        # disabling the next question button until user has correct answer.
        self.next_button.config(state=DISABLED)

        # collecting the different variables required for checking the answers
        score = self.score.get()

        question = self.var_question.get()

        var_new_question_num = self.var_ques_number.get()

        question_num = self.var_question_number.get()

        # dark red for incorrect answer
        answer_wrong = "#F96977"
        # Answer wrong darker text color
        answer_wrong_text = "#A50E1D"
        # dark Green for correct answer
        answer_right = "#18A518"

        # configering the error label to nothing and making the question entry blank
        self.amount_error_label.config(text="")
        self.question_answer_entry.config(bg="white")

        # getting the user and actual answer
        actual_answer = self.var_correct_ans.get()
        user_answer = self.question_answer_entry.get()

        try:
            # checking the users answers against the real answer and also creating the round results which will be
            # carried onto the stats and export function.
            user_answer = int(user_answer)

            # if the users answer is different to the actual answer then inform them it is incorrect
            if user_answer != actual_answer:
                answer_check = "Sorry that is the incorrect " \
                               "answer! Click next to continue"
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)
                self.question_answer_entry.config(bg=answer_wrong)
                self.amount_error_label.config(fg=answer_wrong_text)
                round_results = "Incorrect | {} | You entered:{} | The Correct Answer is:{} | Score:{} / {}".format\
                    (question, user_answer, actual_answer ,score, question_num)
                score = score
                self.round_results_list.append(round_results)

            # if users answer is blank then ask them to enter an answer
            elif user_answer == "":
                answer_check = "You're answer cannot be " \
                               "blank! try again and click submit"
                self.question_answer_entry.config(bg=answer_wrong)
                self.amount_error_label.config(fg=answer_wrong_text)

            # if answer is correct then add 1 point to score and add the
            else:
                answer_check = "Well Done that is the " \
                               "correct answer! Click next to " \
                               "continue"
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)
                self.amount_error_label.config(fg=answer_right)
                self.question_answer_entry.config(bg=answer_right)
                round_results = "Correct | {} | You entered:{} | Score:{} / {}".format(question, user_answer, score,
                                                                                       question_num)
                score = score + 1
                self.round_results_list.append(round_results)
                self.quiz_results_list[1] = score

        except ValueError:
            answer_check= "Please enter a whole number (no text / decimals)"

            self.question_answer_entry.config(bg=answer_wrong)
        self.amount_error_label.config(text=answer_check)

        if var_new_question_num == question_num+1:
            self.amount_error_label.config(text="You have completed the amount"
                                                " of questions you set! click"
                                                " on the stats button to review.")
            self.next_button.config(state=DISABLED)
            self.submit_button.config(state=DISABLED)
        self.score.set(score)

    # setting up for the help button
    def to_help(self):
        get_help = Help(self)

    # so the quit button functions correctly
    def to_quit(self):
        root.destroy()

    # Going to the stats function
    def to_stats(self, round_results, quiz_results):
        QuizStats(self, round_results, quiz_results)


class QuizStats:
    def __init__(self, partner, round_results, quiz_results,):

        partner.stats_btn.config(state=DISABLED)

        heading = " Arial 12 bold"
        content = "Arial 12"

        self.quiz_stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.quiz_stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,
                                                                 partner))

        self.stats_frame = Frame(self.quiz_stats_box)
        self.stats_frame.grid()

        # Set up help heading (row 0)
        self.stats_heading = Label(self.stats_frame, text="Quiz Statistics",
                                   font="arial 19 bold")
        self.stats_heading.grid(row=0)

        self.stats_instructions = Label(self.stats_frame,
                                         text="Here are your Game Statistics."
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10)
        self.stats_instructions.grid(row=1)

        # Frame for the Stats (Row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        self.num_question_label = Label(self.details_frame,
                                        text="Number of Questions: ",
                                        font=heading, anchor="e")
        self.num_question_label.grid(row=0, column=0, padx=1)

        self.percent_label = Label(self.details_frame, font=content,
                                   text="{}"
                                   .format(quiz_results[0]), anchor="w")
        self.percent_label.grid(row=0, column=1, padx=0)

        self.correct_label = Label(self.details_frame,
                                   text="Correct Answers: ", font=heading,
                                   anchor="e")
        self.correct_label.grid(row=1, column=0, padx=1)

        self.correct_label = Label(self.details_frame, font=content,
                                       text="{}"
                                       .format(quiz_results[1]), fg="#27FD36", anchor="w")
        self.correct_label.grid(row=1, column=1, padx=0)

        self.incorrect_label = Label(self.details_frame, font=heading,
                                       text="Incorrect Answers:", anchor="e")
        self.incorrect_label.grid(row=2, column=0, padx=0)

        self.incorrect_label = Label(self.details_frame, font=content,
                                       text="{}"
                                       .format(quiz_results[0]-quiz_results[1]), fg="#FA2828", anchor="w")
        self.incorrect_label.grid(row=2, column=1, padx=0)

        self.percent_label = Label(self.details_frame,
                                    text="Percent of questions correct: ",
                                    font=heading, anchor="e")
        self.percent_label.grid(row=3, column=0, padx=1)

        self.percent_label = Label(self.details_frame, font=content,
                                     text="{:.1f}%"
                                     .format((quiz_results[1] / quiz_results[0])* 100), anchor="w")
        self.percent_label.grid(row=3, column=1, padx=0)

        # Dismiss Button (Row 4)
        self.dismiss_export = Frame(self.stats_frame)
        self.dismiss_export.grid(row=4)

        self.dismiss_btn = Button(self.dismiss_export, text="Dismiss", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=7,
                                  command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=6, column=0, pady=10, padx=5)

        self.export_btn = Button(self.dismiss_export, text="Export", fg="white",
                                 bg="#003366", font="Arial 15 bold", width=7,
                                 command=lambda: self.to_export(quiz_results, round_results))
        self.export_btn.grid(row=6, column=1, pady=10, padx=5)

    def close_stats(self, partner):
        partner.stats_btn.config(state=NORMAL)
        self.quiz_stats_box.destroy()

    def to_export(self, quiz_results, round_results):
        Export(self, quiz_results, round_results)


class Export:
    def __init__(self, partner, quiz_results, round_results):

        # disable export button
        partner.export_btn.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.export_box, width=300, )
        self.stats_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.stats_frame, text="Export / "
                                                         "Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.stats_frame, text="Enter a filename in the "
                                                         "box below and press the "
                                                         "Save button to save your "
                                                         "quiz history to a "
                                                         "text file. ",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning Text Instructions (label, row 1)
        self.export_text = Label(self.stats_frame, text="If the filename you "
                                                         "enter below already "
                                                         "exists, its contents "
                                                         "will be replaced with "
                                                         "your new quiz history ",
                                 justify=LEFT, bg='#ffafaf', fg='maroon',
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        self.filename_entry = Entry(self.stats_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        self.save_error_label = Label(self.stats_frame, text="")
        self.save_error_label.grid(row=5, pady=10)

        self.save_cancel_frame = Frame(self.stats_frame)
        self.save_cancel_frame.grid(row=4)

        # Save and Cancel Buttons (row 0 of save_cancel_frame
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, quiz_results , round_results)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#660000", fg="white",
                                    command=partial(lambda: self.close_export(partner)))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, quiz_results, round_results):

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"
        problem = ""

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"
                has_error = "yes"

            elif letter == ".":
                problem = "(no .'s allowed)"
                has_error = "yes"

            else:
                problem = "(the filename you chose is not valid)"
                has_error = "yes"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.filename_entry.config(bg="#ffafaf")
            self.save_error_label.config(text=problem)

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt
            filename += ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # Heading for stats
            f.write("Game Statistics\n\n")

            # Game stats
            f.write("Number of Questions : {} \n".format(quiz_results[0]))
            f.write("Correct Answers : {} \n".format(quiz_results[1]))
            f.write("Incorrect Answers : {} \n".format(quiz_results[1] - quiz_results[0]))
            f.write("Percentage of correct answers : {:.1f}% \n".format((quiz_results[1] / quiz_results[0])* 100))

            # heading for rounds
            f.write("\nRound Details\n")

            # writing in the questions as well as the user answer adn the correct answer
            for question in round_results:
                f.write(question + "\n")

            f.close()

        self.close_export(partner)

    # for closing export class
    def close_export(self, partner):
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()


class Help:
    def __init__(self, partner):
        # Disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and "releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up help GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # text displayed when help button is pushed
        help_text =("To Play a quiz\n"
                    "First, choose the number of questions and the range, \n"
                    "then choose the type of questions you want to play.\n"
                    "Quiz Rules\n"
                    "Enter an answer in the given space and \n"
                    "then click the 'Submit' button to lock your answer and \n"
                    "as you do that there some feedback will appear about your answer.\n"
                    "Click the 'Next' button to see the next questions.\n"
                    "Quiz Results\n"
                    "To save your results from the quiz\n"
                    "click the 'Export' button and \n"
                    "then enter a valid file name and click  on the 'Save' button.\n")

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss Button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    # for closing the help
    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()
