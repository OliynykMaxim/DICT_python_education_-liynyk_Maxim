import random

print("HANGMAN")
print("The game will be available soon.")
words = ["python" , "java" , "php" , "html"]
word = random.choice(words)
a = input("Guess the word :\n>")
while True:
   if a == word: