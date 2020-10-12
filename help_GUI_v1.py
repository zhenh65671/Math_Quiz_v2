from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self.maths_quiz_label = Label(self.start_frame, text="Maths Quiz",
                                       font="Arial 19 bold")
        self.maths_quiz_label.grid(row=1)

        # Help Button (row 2)
        self.help_button = Button(self.start_frame, text="help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=2)

    def help(self):
        print("you asked for help")
        get_help = Help(self)

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

        help_text="Choose an amount to play with and then choose the level.  " \
                  "It have three different levels, addition, subtraction" \
                  "and multiplication \n\n" \
                  "When you enter the play area, you will see the question " \
                  "and a box next to it. Than you can push the submit you answer," \
                  "after you checked your answer you can go to the next question."\
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
    root.title("Maths Quiz")
    something = Start(Start)
    root.mainloop()