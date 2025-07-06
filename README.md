# Hangman Game

#Introduction
 
The Hangman game is a classic word-guessing game where players try to guess a secret word letter 
by letter before running out of attempts. This version of the game is implemented using Python and Tkinter 
to provide a graphical user interface.

#Features

1.Three difficulty levels: Easy, Medium, and Hard

2.Hints for each word

3.Score tracking

4.Graphical user interface with Tkinter

5.Celebration message on winning

#Installation
To run this game, ensure you have Python installed on your system. You also need Tkinter,
which comes pre-installed with Python.

1.Install Python (if not already installed) from python.org

2.Download or copy the Hangman game script.

3.Run the script using the following command: hangman.py


#How to Play

1.Choose a difficulty level (Easy, Medium, Hard).

2.A word is randomly selected, and its hint is displayed.

3.Guess letters one at a time.

4.Correct guesses reveal letters in the word.

5.Incorrect guesses reduce the number of attempts left.

6.The game ends when you either guess the word correctly or run out of attempts.

#Code Explanation

1.Word Selection: The game randomly picks a word from a predefined dictionary based on the chosen difficulty.

2.Game State Management: The game tracks the secret word, guessed letters, remaining attempts, and score.

3.User Input Processing: The program checks if the guessed letter is in the word and updates 
the game state accordingly.

4.Implementation: Tkinter is used to create buttons, labels, and input fields for an interactive experience.

5.Winning and Losing Conditions: If the player guesses all letters correctly, a celebration message appears. 
If the player runs out of attempts, the game displays the correct word.

#Future Improvements

1.Add more words with hints to expand the game.

2.Save high scores and allow users to view them.

3.Create a multiplayer mode.

4.Integrate MySQL for secure user data storage.
