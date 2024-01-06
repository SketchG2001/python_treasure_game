from hangman_words import word_list
import random
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
word_length = len(chosen_word)
lives = 6

from hangman_art import logo,stages,logo1
print(logo)
for _ in range(word_length):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    if guess in display:
        print(f"You've already guessed{guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"current position is {position}\n "
        #       f"current letter is {letter}\n"
        #       f"Guessed letter: {guess}")
        if letter == guess:
            print("Right")
            display[position] = letter
        if guess not in chosen_word:
            print(f"you guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(logo1)
    print(f"{' '.join(display)}")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])