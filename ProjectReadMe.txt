Readme for Project_Bonjun_Koo.py

Before continuing, ensure that you have met the following requirement:
-You have installed a python intepreter, preferably a newer version 3.8.2+

Once you have downloaded PA3_Bonjun_Koo.py, open up the command prompt (Windows) or terminal (MacOS).

HOW TO RUN THE PROGRAM:
Before proceeding with command line arguments, make sure you are in the correct directory/path
-To get into the correct directory, you may use the command "cd \Path\Example\folder"

Then, you can run the program through the command "py Project_Bonjun_Koo.py"

1. Once the program launches, you will be prompted to submit the number of bot players you wish to play with. Standard Texas Holdem Poker tables typically
have a limit on how many players can play, so the limit for this program will be 9 other bots (10 total players including the user). Once you enter the
number of players desired, you may click the enter button to proceed.

2. Each player has a name and 4 assigned label/text boxes assigned to it. The two big text boxes under the players' name represent their two cards and the two
   smaller boxes represent the player's money and bet amount. The smaller left box represents the amount of money the player currently holds. The right
   smaller box represents the total bet amount the player has.

3. Once the game begins, you will have 3 action options.
	-Check: Check can only be used for the first move and results in the player not betting anything and directly proceeding to the second round

	-Fold: The player folds and gives up all bets made up to the point of the fold action. The player is now no longer considered part of that 1 game
		cycle and can not win. They will be added to the next game cycle. If the player has no money, they should bet 0 dollars.

	-Bet: The player can bet a certain amount of money. The player can only bet up to the amount of money that they currently have. There is a text
		entry box right above the bet button in which the player must input the amount of money they wish to bet. It must be a number and if it is not
		the program will prompt it for a number

4. The winner of each game will be displayed in the big white text box located near the bottom left of the window. If a bot player is out of money, they will
be removed from the game and their text boxes will become blank, indicating that they are no longer a part of the game.

5. After each game, the player will have the option to play again or to quit. The play again button will start a new game cycle then the quit and play again
button will become inaccessible so the player cannot use it during the game. The quit button will close the GUI and stop the game. If the player has no money
they will only be allowed to quit the GUI.




