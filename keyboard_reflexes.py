# Importing libraries
import time
import random
import string
import curses

# Preparing to start the game, displaying instructions and asking user to proceed. Using the stdscr.getch() function from the curses library to get user input through the press of a key. Exiting terminal to prepare to start the game when user input is received.
def instructions():
	stdscr = curses.initscr()
	curses.echo()
	stdscr.addstr(("Quickly press the key that is displayed on the screen. Get 5 points to win. Press E to proceed."))
	key = stdscr.getch()
	while str(key) != str(ord('e')):
		key = stdscr.getch()
		curses.noecho()
	curses.endwin()
	stdscr.erase()

# Function that initiates game, prompts user until score reaches 5. Verifying user input when key is pressed, as well as tracking user score and response time (gets added to the total time for each point/iteration).
def init_game():
	score = 0
	totalTime = 0
	response_time = 0
	alphabet = list(string.ascii_lowercase)

	while score < 5:
		selection = random.choice(alphabet)
		curses.noecho()
		stdscr = curses.initscr()
		stdscr.addstr(selection.upper())
		start_time = time.time()
		key = stdscr.getch()
		
		while str(key) != str(ord(selection)):
			stdscr.refresh()
			key = stdscr.getch()
			
		score += 1
		end_time = time.time()
		response_time = round((end_time - start_time), 3)
		totalTime += response_time
		
		curses.echo()
		print("\n\n+1 points")
		print("\nCurrent score: {0}".format(str(score)))
		print("\nResponse time: {0}".format(str(response_time)))
		
		stdscr.refresh()
		curses.noecho()
		time.sleep(0.75)
		stdscr.move(0, 0)
		stdscr.erase()
		curses.endwin()
	print("Game over. Total time:", totalTime)

# Displaying instructions, starting game
instructions()
init_game()
