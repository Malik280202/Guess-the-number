import random

top_of_range = input('Type a number: ')
if top_of_range.isdigit:
    top_of_range = int(top_of_range)

    if top_of_range <= 0: print('type a bigger number next time!')
    else:
        print('type a smaller number next time')

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_input = input('Make a guess: ')
        if user_input.isdigit():
            user_input = int(user_input)
        else:
            print('type a larger number next time')
        
        if user_input == random_number: print('you got it'); break
        elif user_input > random_number: print('you were above the number!')
        else:
            print('you were below the number!')
print('You got', guesses,'times')