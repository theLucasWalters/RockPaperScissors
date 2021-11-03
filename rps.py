import random

# setup
my_choices = ['rock', 'paper', 'scissors', 'mnms']
bot_choices = ['rock', 'paper', 'scissors']

# game
while True:
    my_choice = input("Enter rock, paper, or scissors > ")

    # check if they want to quit or if they enter something invalid
    if my_choice == 'quit':
        quit()
    elif my_choice not in my_choices:
        print("You can't choose that!")
        quit()

    # bot chooses randomly
    bot_choice = random.choice(bot_choices)

    # display what the player and bot chose
    print(f"You chose: {my_choice}")
    print(f"The bot chose: {bot_choice}")

    # determine if it's a win or loss
    if my_choice == 'rock' and bot_choice == 'scissors':
        print("You won!")
    elif my_choice == 'paper' and bot_choice == 'rock':
        print("You won!")
    elif my_choice == 'scissors' and bot_choice == 'paper':
        print("You won!")
    elif my_choice == 'mnms':
        print('You won!')
        print('MnM\'s always win.')
    elif my_choice == bot_choice:
        print("A tie!")
    else:
        print("You lost :(")
