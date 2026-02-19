from enigma import *
import curses
import time
stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)





begin_x = 0
begin_y = 0
height = curses.LINES
width = curses.COLS
win = curses.newwin(height, width, begin_y, begin_x)
curses.echo()            # Enable echoing of characters

# Get a 15-character string, with the cursor on the top line
s = stdscr.getstr(0,0, 500)
while True:
    c = stdscr.getch()
    if c == ord('q'):
        break  # Exit the while loop
stdscr.refresh()



curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
print(s)