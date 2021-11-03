import random

# setup
times_rock = 0
times_paper = 0
times_scissors = 0

player_win = 0
bot_win = 0
tie = 0

def display_counts():
    print(f"You: {player_win} Bot: {bot_win} Ties: {tie}")

def tie():
    print("A tie!")
    display_counts()

def win():
    print("You won!")
    display_counts()

def lose():
    print("You lost...")
    display_counts()

def error(*args):
    raise Exception(f"Something went wrong: {args}")

all_choices = ['rock', 'paper', 'scissors']

# other arrays the bot needs to choose from
paper_scissors = ['paper', 'scissors']
rock_paper = ['rock', 'paper']

# the actual game
while True:
    player_choice = input("Choose Rock, Paper, or Scissors > ").lower()

    # check that the player's choice is legitimate
    if player_choice not in all_choices:
        print("Must be Rock, Paper, or Scissors.")
    else:
        # if it is, run the bot choice algorithm
        # this works by using the number of times a player has used a certain move to play
        # a more likely winning move
        if times_rock == times_paper and times_rock == times_scissors:
            bot_choice = random.choice(all_choices)

        elif times_rock == times_paper and times_rock > times_scissors:
            bot_choice = random.choice(paper_scissors)

        elif times_rock > times_paper and times_rock == times_scissors:
            bot_choice = random.choice(rock_paper)

        elif times_rock > times_paper and times_rock > times_scissors:
            bot_choice = all_choices[1]

        elif times_paper > times_rock and times_paper > times_scissors:
            bot_choice = all_choices[2]

        elif times_scissors > times_rock and times_scissors > times_paper:
            bot_choice = all_choices[0]

        else:
            error(times_rock, times_paper, times_scissors)

        # display what the player and the bot chose
        print(f"You chose: {player_choice}")
        print(f"The bot chose: {bot_choice}")

        # if the player won, increment their win count
        # and the same for a bot win or a tie
        if player_choice == bot_choice:
            tie += 1
            tie()
        
        elif player_choice == 'rock' and bot_choice == 'scissors':
            player_win += 1
            win()

        elif player_choice == 'rock' and bot_choice == 'paper':
            bot_win += 1
            lose()

        elif player_choice == 'paper' and bot_choice == 'rock':
            player_win += 1
            win()

        elif player_choice == 'paper' and bot_choice == 'scissors':
            bot_win += 1
            lose()

        elif player_choice == 'scissors' and bot_choice == 'paper':
            player_win += 1
            win()

        elif player_choice == 'scissors' and bot_choice == 'rock':
            bot_win += 1
            lose()

        else:
            error(player_choice, bot_choice)

        # this is where the bot 'learns' what the player prefers
        match player_choice:
            case 'rock':
                times_rock += 1
            case 'paper':
                times_paper += 1
            case 'scissors':
                times_scissors += 1
            case _:
                error(player_choice)
