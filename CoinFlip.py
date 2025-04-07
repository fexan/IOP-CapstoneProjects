'''
Author: Ifeoluwa Oyelowo-Paul
Date: April 4, 2025


Coin Flip Simulation:

Code simulates flipping a single coin however many times decided by the user. 
The code records the outcomes and counts the number of tails and heads.
'''

import random


# Ask User how many times they'll like the coin to be flipped -- flip_count
# Use while loop to ensure input is an int

flip_count = 0

while True:
    try:
        flip_count = int(input("How many times will you like the coin to be flipped? (Must be an integer): "))
    except:
        print("Input must be an integer. Try again.")
        continue # go back to start of loop

    if flip_count < 0:
        print("Input must be a positive integer > 0. Try again.")
        continue # go back to start of loop

    break # break if there is no error


# Use a counter to keep track of the number of times flipped. for loop from 1 to flip_count
heads = 0
tails = 0

for i in range(1,flip_count+1):
    # flip coin
    coin = random.randint(0,1)
    # Use heads and tails vars to keep track of outcome of coinflip
    if coin == 0:
        tails+=1
    else:
        heads+=1


# print result
print(f"The coin was flipped {flip_count} times.")
print(f"Heads:{heads}. Tails:{tails}")