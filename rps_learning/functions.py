# displays the player_win, bot_win, and tie counts
def display_counts(player_win, bot_win, tie):
    print(f"You: {player_win} Bot: {bot_win} Ties: {tie}")

# displays a tie
def tie(player_win, bot_win, tie):
    print("A tie!")
    tie += 1
    display_counts(player_win, bot_win, tie)

# displays a win
def win(player_win, bot_win, tie):
    print("You won!")
    player_win += 1
    display_counts(player_win, bot_win, tie)

# displays a loss
def lose(player_win, bot_win, tie):
    print("You lost...")
    bot_win += 1
    display_counts(player_win, bot_win, tie)

# custom error if something goes wrong
def error(*args):
    raise Exception(f"Something went wrong: {args}")
