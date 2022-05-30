import random

def guess(x):
    """
    The function takes a number as an argument and generates a random number between 1 and the number
    passed as an argument. The user is then prompted to guess the number. If the user guesses the number
    correctly, the function prints a congratulatory message. If the user guesses incorrectly, the
    function prints a message indicating whether the guess was too high or too low
    
    :param x: the number of guesses you want to have
    """
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again too low')
        elif guess > random_number:
            print('Sorry, guess again too high')
    print(f'You have guessed a correct number  {random_number} !Congrats.')

# Calling the function guess with the argument 10.
# guess(10)

def computer_guess(x):
    """
    The computer guesses a random number between 1 and the number you chose. If the guess is too high,
    the computer will guess a random number between 1 and the guess. If the guess is too low, the
    computer will guess a random number between the guess and the number you chose. If the guess is
    correct, the computer will tell you it guessed correctly
    
    :param x: the number of possible guesses
    """
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number, {guess}, correctly.')

computer_guess(100)