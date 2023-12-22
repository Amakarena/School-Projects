The purpose of my project was to create a fighting game with the cute, loveable, and generally (Kuromi is an exception sometimes) non-violent Sanrio characters. It's a program reminiscent of the Discord game pokeduel where users can fight in pokemon battles with a (cheating) computer.

This is a text-based game and I decided to make it that way because I have the most experience with it and couldn't think of how to make the game into a website with the time constraint I had. I knew that I wanted to include art in the game, and since it's text-based, ascii art was the way to go. I utilized websites like https://emojicombos.com/ and https://patorjk.com to reach this end.

Here's a general walk through of the design of the game.

START
The game starts with the title card (made with ascii art) and then asks the user to chose a fighter. I utilize 2 important functions here that will continue to be used throughout the code: line_printer and get_input().
line_printer() was my solution to the prompts being written to fast in the terminal. The function basically prints a line and then uses time (which is imported) to wait a few seconds (well, half seconds) depending on how long the string is. It optionally takes the end='' argument as well for prompts where I don't want to start on a new line. This function was originally a char_printer function, so it would print words character by character, however, this feature brough a slew of display problems since the vs code terminal allows users to type things even when not prompted (this, notably, is not an issue in the terminal/command-prompt apps that computers come with).
get_input() uses a function that I got from stack overflow called flush_input and handles the issue where since vs code allows users to type whenever, the regular input() would count whatever nonsense the user typed as a part of the user's input. Basically, get_input() is used in place of input() and clears (flushes) whatever the user typed in previously/doesn't count it as a part of the input.

With the character selection, I used a list of fighters and iterated through it and printed each one out line-by-line in order to minimize repetitive code. When it comes to the drawings, I used code provided to me by chat.gpt that maps fighter names to specific functions that handle the attack moves and drawing of the fighter in ascii art by creating a dictionary that uses the fighter's names as key words and the draw function and attack list as values. Then using the name of the fighter that the user (and then the same for the fighter that the computer) selected, I was able to have the program grab the correct fighting moves and draw the correct image.

For the attack moves, I used a csv file because it made it easier for me to assign certain attacks to certain characters and to assign certain attacks to specific damages and weights (weight is the liklihood that an attack is chosen out of 1000 (225/1000 = 22.5% chance). In the spirit of the randomness of Discord's pokeduel, I made it so that stronger attacks are just as likely as weaker attacks. Except for stun attacks, because those are slow)
    speaking of stun attacks, I decided to assign their point damage within the python file and not in the csv files because all stun attacks have the same damage, and it was easier to handle that in the pyton file than to go and edit every csv file and how the python file read them.

FIGHTING
Since most of this is explained in my code, I will do a bullet note run down here.
* each fighter starts with 100HP (health points)
* i used pl_turn as a boolean to keep track of whose turn it was and a while loop to go back and forth between fighters
* the user has a flower next to their action prompt message so that they can easily identify what moves were theirs and what moves were the cpu's
* With my handle_hit function, I was able to see whether or not an attack would hit or if the fighter would get hit
** the handle_hit function uses rnd.choice to account and added weights to account for whether or not a fighter gets hit
* The attacks made are randomly selected, unlike the character selector where users got to chose, in order to speed up gameplay and to prevent users from selecting their strongest attacks each time. This is also in the fashion of pokeduel
* the damage of each hit is grabbed from the csv file and subtracted from the opponent's health

GAME OVER
Once a fighter's health is at or below 0, the fighting loop terminates and the winner is printed out, ending the main() function. After I call main() I have a while loop that runs the function play_again() which asks the user if they want to play again and returns True or False depending on their answer (if False, a thank you message is given to the user). The while loop will call main() if play_again returns True and terminate if it doesn't.
