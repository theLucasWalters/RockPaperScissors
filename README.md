# Rock Paper Scissors bot(s)
I was teaching my little sister how to code and someone suggested
I help her make a command line Rock, Paper, Scissors game. Along with helping her with that,
I decided to make a couple of my own.<br>
Both run in the command line and were written in Python version 3.10.0.

### `rps.py`
This one is a run-of-the-mill bot that chooses moves randomly using the Python random module.
Simple and fun.

### `rps_learning`
This bot 'learns' the biases of the player and tries to play moves that will be more
statistically likely to beat the player. i.e. if the player tends to use `rock` more,
it will be stored in a variable and the bot will play `paper`.

The game is in `main.py` inside the `rps_learning` folder.
The functions used are in `functions.py`.
