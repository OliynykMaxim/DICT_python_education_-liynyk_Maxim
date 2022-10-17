import random

print("HANGMAN")
print("The game will be available soon.")
word = ["python"]
a = input("Guess the word :\n>")
while True:
    if a == word:
        print("You survived!")
        break
    else:
        print("You lost!")
        break