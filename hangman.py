import random
from words import words
import string

def get_valid_word(words):
    """
    It returns a random word from the list of words, but only if the word doesn't contain a dash or a
    space
    
    :param words: a list of words
    :return: A random word from the list of words.
    """
    word = random.choice(words)
    while '-' in word or ' ' in words:
        word = random.choice(words)
    
    return word

def hangman():
    """
    The function hangman() takes a word from the list of words, and then asks the user to guess a
    letter. If the letter is in the word, it is displayed. If the letter is not in the word, the user is
    asked to guess again. The user has 6 guesses.
    """
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives ,'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))  

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        
        else:
            print('Invalid character. Please try again.')
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:    
        print('You guessed the word', word,'!!')


hangman()