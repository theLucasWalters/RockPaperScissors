import random

myChoices = ['rock', 'paper', 'scissors', 'mnms']
botChoices = ['rock', 'paper', 'scissors']

while True:
    myChoice = input("Enter rock, paper, or scissors > ")

    if myChoice == 'quit':
        quit()
    elif myChoice not in myChoices:
        print("You can't choose that!")
        quit()

    botChoice = random.choice(botChoices)

    print(f"You chose: {myChoice}")
    print(f"The bot chose: {botChoice}")

    if myChoice == 'rock' and botChoice == 'scissors':
        print("You won!")
    elif myChoice == 'paper' and botChoice == 'rock':
        print("You won!")
    elif myChoice == 'scissors' and botChoice == 'paper':
        print("You won!")
    elif myChoice == 'mnms':
        print('You won!')
        print('MnM\'s always win.')
    elif myChoice == botChoice:
        print("A tie!")
    else:
        print("You lost :(")
