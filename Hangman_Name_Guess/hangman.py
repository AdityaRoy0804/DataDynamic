import random
import hangman_stages
import words_file
print("This is name guess word game (you got 6 lives ).")
chosen_word = random.choice(words_file.words)
lives = 6
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guess_letter = input("guess a letter:")
    for i in range(len(chosen_word)):
        if guess_letter == chosen_word[i]:
            display[i] = guess_letter
    print(display)
    if guess_letter not in chosen_word:
        lives = lives - 1
        if lives == 0:
            game_over = True
            print("You Lose.")
    if '_' not in display:
        game_over = True
        print("You Won !!")
    print(hangman_stages.stages[lives])
          