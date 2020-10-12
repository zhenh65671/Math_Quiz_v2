import random

for item in range(0, 2):
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)

    question = "{} * {}".format(num_1, num_2)
    display_question = "{} × {} = ".format(num_1, num_2)

    user_ans = int(input(display_question))

    answer = eval(question)

    if user_ans == answer:
        print("ok")
    else:
        print("oops")

