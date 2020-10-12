from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class quiz:
    def __init__(self, ):

        # Formatting variables...
        self.quiz_history = []

        # In actual program this is blank and is populated with user calculations
        self.quiz_results = ['1/10']

        self.quiz_frame = Frame()
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Quiz Stats",
                                   font="Arial 19 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # history Button (row 1)
        self.stats_button = Button(self.quiz_frame,
                                   font="Arial 14", padx=10, pady=10, text="Push me",
                                   command=lambda: self.to_stats(self.quiz_history, self.quiz_results))
        self.stats_button.grid(row=1)

    def to_stats(self, quiz_history, quiz_results):
        quizStats(self, quiz_history, quiz_results)


class quizStats:
    def __init__(self, partner, quiz_history, quiz_results):

        # disable history button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window  (ie: stats box)
        self.quiz_results_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.quiz_results_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.quiz_results_box)
        self.stats_frame.grid()

        # Set up history heading (row 0)
        self.stats_heading = Label(self.stats_frame, text="Quiz Statistics",
                                 font="arial 19 bold")
        self.stats_heading.grid(row=0)

        # To export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Quiz Statistics."
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played", wrap=300,
                                         font="Arial 10 italic", justify=LEFT, fg="maroon")
        self.export_instructions.grid(row=1)

        # Frame for the Quiz stats (row 2)
        self.detail_frame = Frame(self.stats_frame)
        self.detail_frame.grid(row=2)

        # Amount of question played
        self.score_label = Label(self.detail_frame,
                                        text="Score: ",
                                        font=heading, anchor="e")
        self.score_label.grid(row=0, column=0, padx=1)

        self.percent_label = Label(self.detail_frame, font=content,
                                   text="{}"
                                   .format(quiz_results[0]), anchor="w")
        self.percent_label.grid(row=0, column=1, padx=0)

        self.correct_label = Label(self.detail_frame,
                                   text="Correct Answers: ", font=heading,
                                   anchor="e")

        # Round Played (row 2.4)
        self.quiz_played_label = Label(self.detail_frame,
                                       text="questions Played:", font=heading,
                                       anchor="e")
        self.quiz_played_label.grid(row=4, column=0, padx=0)

        self.quiz_played_value_label = Label(self.detail_frame, font=content,
                                             text=len(quiz_history),
                                             anchor="w")
        self.quiz_played_value_label.grid(row=4, column=1, padx=0)

        # Dismiss Button (row 3)
        self.export_dismiss_frame = Frame(self.stats_frame)
        self.export_dismiss_frame.grid(row=3)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 15 bold", bg="#003366", fg="white",
                                    command=lambda: self.export(quiz_history, quiz_results))
        self.export_button.grid(row=0, column=0, padx=5)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Cancel",
                                     font="Arial 15 bold", bg="#660000", fg="white",
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1, pady=10)

    def close_stats(self, partner):
        # Put help button back to normal...
        partner.stats_button.config(state=NORMAL)
        self.quiz_results_box.destroy()

    def export(self, quiz_history, quiz_stats):
        Export(self, quiz_history, quiz_stats)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box quiz")
    something = quiz()
    root.mainloop()