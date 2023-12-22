Hello, welcome to Sanrio Showdown! This game is simply for entertainment and not at all leagally connected to the actual Sanrio Company.
Read me in order to get an idea on how to access and play the text-based fighting game!

SET UP
1. You should have recieved a zip folder called "project.zip" You need to download it and REMEMBER WHAT FOLDER YOU DOWNLOADED IT INTO
    (be it your "Downloads" or "Documents" or whatever folder). Let's call this folder Location
2. Go to (but not INTO) the project.zip folder and right-click on the zipped folder. Then click "Extract All" which should create a new unzippedfolder within Location called "project"
3 (IF USING VS CODE OR SOMETHING SIMILAR). Open VS Code and click on the "open folder" option on your homescreen. Select "project." If not on homescreen, then drag the "project" folder from your files to the "EXPPLORER" section to the left side of your screen.
3 (IF NOT USING VS CODE OR SOMETHING SIMILAR). Now, you need to open up your computer's terminal. If you don't know where that is, go to your search bar (which if not on your taskbar, you can use the one in your settings) and search for "Terminal"
4. Once you have your terminal open, enter your Location folder and THEN the project folder like so:
$ cd location
\Location$ cd project
($ might be > on your computer)
(IF ON VS CODE OR SMT SIMILAR, you can just do "$cd project")
(there may be some words before the $, that's typically just outlining who the user is. If you're already within another folder, exit out of that with "cd.." and if that doesn't work then use "cd")
5. You'll know that you're in if your terminal now has "project\ $" or "project/ $" at the start of each new line
6. Type in the command "python sanrio_showdown.py" (make sure that "project/ $" at the start of each line, or else your computer won't know what you're talking about!)
    * If python command isn't recognized, see 2 in "QUESTIONS/PROBLEMS THAT MIGHT ARISE" section of this file
7. The game should start! The game is entirely run within the terminal

GAMEPLAY
Gameplay is fairly simple. Just follow the instructions given the program! (It can be quite mean if you don't).

QUESTIONS/PROBLEMS THAT MIGHT ARISE
1. "How to exit out of the game?" Press Ctrl + Z or say no/n when asked if you want to play again
2. "My terminal doesn't know what python is." In this case, it's likely not downloaded. To fix this, go to https://www.python.org/downloads/ and click the big yellow button (make sure it's for the right software macos/windows!). Python should then download, and once it does, go to your downloads and open it. Make sure to give it admin permissions if it asks/click the two empty boxes if they're empty. Then install normally (don't do custom install unless you're familar with Python). You should get a message telling you that it has successfully been installed. *THEN* close your terminal, reopen it, and then do all of the steps in SET UP
3. "I don't have a terminal/The terminal isn't working." Try searching for/using "Command Prompt" instead
4. "I'm getting an error about cpu_attack_file not having a value." ahahahahaha that shouldn't happen (like, it *really* shouldn't), but if it does, exit out of the game and restart.
5. "I tried to copy something while the game was running and used Ctrl + C and the game stopped!" That's a feature of terminals, not a bug. Similar to Ctrl + Z and how it exits out of programs, Ctrl + C is meant to interupt programs.

And you should be all set! Have fun!
