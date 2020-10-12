import random

NUM_QUES = 5

for item in range(0,10):

    lo_num = 1
    hi_num = 12
    operator = "-"
    display_text = "-"

    # generate question
    num_1 = random.randint(lo_num, hi_num)
    num_2 = random.randint(lo_num, hi_num)

    if num_1 < num_2:
        num_1, num_2 = num_2, num_1

    question = "{} {} {}".format(num_1, operator, num_2)
    display_question = "{} {} {} = ".format(num_1, display_text, num_2)
    answer = eval(question)

    print("{} {}".format(display_question, answer))

