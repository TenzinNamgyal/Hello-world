# print("Welcome to Guess the Number!")
# print("The rules are simple. I will think of a number, and you will try to guess it.")
# import random
# number = random.randint(1,10)# Random number between 1 to 10
# isGuessRight = False
# #START OF WHILE LOOP
# while isGuessRight != True:
#     guess = input("Guess a number between 1 and 10: ")# GAVE INPUT
#     if int(guess) == number:
#         print("You guessed {}. That is correct! You win!".format(guess))
#         isGuessRight = True
#     else:
#         print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))# INPUT
print("Count to 10!")
for x in range (0, 11):# FOR LOOP
    print(x)#Print of number