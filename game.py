from questions import questions
from answers import answers
import time
import random

correct_answers = 0
playing = True
while playing:
    question = random.choice(questions) 
    if question == questions[0]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[0])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(2) or answer == answers[0][1].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[0][1]}.")
            time.sleep(1)

    if question == questions[1]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[1])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(3) or answer == answers[1][2].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[1][2]}.")
            time.sleep(1)

    if question == questions[2]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[2])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(3) or answer == answers[2][2].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[2][2]}.")
            time.sleep(1)

    if question == questions[3]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[3])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(3) or answer == str(2) or answer == answers[3][2].lower() or answer == answers[3][1].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[3][2]}\nor\n{answers[3][1]}.")
            time.sleep(1)

    if question == questions[4]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[4])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(3) or answer == answers[4][2].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[4][2]}.")
            time.sleep(1)

    if question == questions[5]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[5])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(2) or answer == answers[5][1].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[5][1]}.")
            time.sleep(1)

    if question == questions[6]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[6])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(1) or answer == answers[6][0].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[6][0]}.")
            time.sleep(1)

    if question == questions[7]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[7])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(2) or answer == answers[7][1].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[7][1]}.")
            time.sleep(1)

    if question == questions[8]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[8])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(1) or answer == answers[8][0].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[8][0]}.")
            time.sleep(1)

    if question == questions[9]:
        print("-------------------------------------------------")
        print("\nQuestion:")
        print(question)
        print("\nOptions:")
        for index, options in enumerate(zip(answers[9])):
            print(f"{index+1}. {options}")
        answer = input("\nYour answer [1, 2, 3]: ").lower()
        if answer == str(3) or answer == answers[9][2].lower():
            time.sleep(1)
            print("Woo hoo, your answer is correct!")
            time.sleep(1)
            correct_answers += 1
        else: 
            time.sleep(1)
            print(f"No, the correct answer is {answers[9][2]}.")
            time.sleep(1)

    
        time.sleep(2)
        play_again = input("\nDo you want to play again? [y/n]: ")
        if play_again == "y":
            print("Loading...")
            time.sleep(3)
            continue
        else:
            print("Closing the game...")
            time.sleep(1)
            playing = False


print(f"Your score: {correct_answers}/10 correct answers.") 
