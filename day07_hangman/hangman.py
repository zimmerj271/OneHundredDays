import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ['_'] * word_length


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
guessed_letters = []
print(stages[lives])
while not end_of_game:
    print(display)
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    elif guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word.  You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
    else:
        for idx, char in enumerate(chosen_word):
            if char == guess:
                display[idx] = guess
        if '_' not in display:
            end_of_game = True
            print("You WIN!")
            print(display)

    guessed_letters.append(guess)
    print(stages[lives])
    