import random

print("HANGMAN")
print("The game will be available soon.")
my_list = ["html", "java", "php", "python"]
my_word = random.choice(my_list)
remember_letters = []
all_letters = list(set(my_word))
word = "".join([i if i in remember_letters else "_" for i in my_word])
print(word)
life = 8
while life > 0:
    letter = input("Input a letter:")
    if letter in my_word and letter not in remember_letters:
        remember_letters.append(letter)
        all_letters.remove(letter)
    if letter not in my_word:
        life -= 1
        print("That letter doesn't appear in the word")
    if letter in remember_letters:
            life -= 1
            print("No improvements")
    word = "".join([i if i in remember_letters else "_" for i in my_word])
    print(word)
    if life == 0 and len(all_letters) != 0:
        print("You lose!")
    if len(all_letters) == 0:
        print("You win!")
        break

print("thanks for playing\nWe'll see how well you did in the next stage")