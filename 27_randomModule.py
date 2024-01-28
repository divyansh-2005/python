import random
# print(help(random))
# low = 1
# high = 100
# options = ("rock", "paper", "sissors")
# cards = ["2", "3", "4", "K", "Q", "J", "A"]

# number = random.randint(low,high) #generates random interget from low to high

# number = random.random()
# print(number)

# option = random.choice(options)
# print(option)

# random.shuffle(cards)
# print(cards)


# Generate random numbers 
low = 1
high = 100
guesses = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!")
        break

print(f"Number of guess: {guesses}")
                