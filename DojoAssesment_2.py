import random

# Generating random numbers in an array using randint
random_code = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
print(random_code)

attempts = 0

# While the user is in the round <12 he can play. The number of attepmts increments everytime the users completes entering the four numbers
while attempts < 12:
    attempts += 1

    print("This is attempt: ", attempts)
    print("Enter numbers (between 1 and 6): ")

    # Getting User Inputs
    inputs = [] # initial state for the inputs list
    for i in range(4): 
        user_input = 0 # inital state for the user input
        while user_input not in range(1, 7):
            user_input = int(input("Number " + str(i + 1) + ": "))
        inputs.append(user_input)

    # Comparing user inputs to the random code
    correct = 0
    wrong_position = 0

    for i in range(4):
        if inputs[i] == random_code[i]:
            correct += 1
        elif inputs[i] in random_code:
            #if inputs.count(inputs[i]) <= random_code.count(inputs[i]): This is my approach on how I wanted to fix it but it just didn't work.
                wrong_position += 1

    print("Correct guesses: ", correct)
    print("Correct numbers in wrong position: ", wrong_position)

    # Checking if the user has guessed everything correctly
    if correct == 4:
        print("You won!")
        break
else:
    print("You have used all attempts")