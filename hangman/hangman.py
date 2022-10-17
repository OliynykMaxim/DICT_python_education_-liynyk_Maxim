import random

print("HANGMAN")
print("The game will be available soon.")
my_list = ["html", "java", "php", "python"]
my_word = random.choice(my_list)
remember_letters = []
input_letters = []
all_letters = list(set(my_word))
word = "".join([i if i in remember_letters else "_" for i in my_word])
print(word)
life = 8
while life > 0:
    letter = input("Input a letter:")
    if letter == letter.lower() and len(letter) == 1:
        if letter in my_word and letter not in remember_letters and letter not in input_letters:
            remember_letters.append(letter)
            all_letters.remove(letter)
        elif letter in remember_letters or letter in input_letters:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            life -= 1
        word = "".join([i if i in remember_letters else "_" for i in my_word])
        print(word)
        if len(all_letters) == 0:
            print("You guessed the word\nYou survived!")
            break
    elif letter != letter.lower():
        print("Please enter a lowercase English letter")
    elif len(letter) != 1:
        print("You should input a single letter")
if len(all_letters) > 0:
    print("You lost!")