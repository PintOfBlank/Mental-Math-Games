import random
import operators
import time

print("_______________________________________________________________")
print("_______________________________________________________________")
print("  __  __            _        _   __  __       _   _         _ \n"
      " |  \/  | ___ _ __ | |_ __ _| | |  \/  | __ _| |_| |__  ___| |\n"
      " | |\/| |/ _ \ '_ \| __/ _` | | | |\/| |/ _` | __| '_ \/ __| |\n"
      " | |  | |  __/ | | | || (_| | | | |  | | (_| | |_| | | \__ \_|\n"
      " |_|  |_|\___|_| |_|\__\__,_|_| |_|  |_|\__,_|\__|_| |_|___(_)\n"
      "                                                              ")
print("_______________________________________________________________")
print("_______________________________________________________________")

start = str(input("\n1. Start\n2. Quit\n\nChoice: "))

while True:
    if start == "2":
        quit()
    elif start == "Quit":
        quit()
    elif start == "quit":
        quit()
    elif start == "1":
        break
    elif start == "Start":
        break
    elif start == "start":
        break
    else:
        print("Try Again!")

rounds = int(input("\nHow Much Times Do You Wanna Play?\n\nChoice: "))

display_operators = ["+", "-", "×"]
score = 0
overall_time = []

for i in range(1, rounds+1):
    number1 = random.randint(1, 10)
    operator_between = random.choice(display_operators)
    number2 = random.randint(1, 10)

    global answer

    if operator_between == display_operators[0]:
        answer = operators.add(number1, number2)
    elif operator_between == display_operators[1]:
        answer = operators.minus(number1, number2)
    elif operator_between == display_operators[2]:
        answer = operators.multiply(number1, number2)

    print("")
    print(number1, operator_between, number2)
    user_answer_timer = time.perf_counter()
    user_answer = int(input("> "))
    user_answer_timer_after = time.perf_counter()
    overall_time.append(user_answer_timer_after-user_answer_timer)

    if user_answer == answer:
        print("\nCorrect!")
        score += 1
    elif user_answer != answer:
        print("\nWrong")

summed_overall_time = sum(overall_time)
print(f"\nYour Time Was {summed_overall_time:0.2f} Seconds!")
print(f"\nYour Score Was {score}/{rounds}!")
