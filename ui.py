from enigma import *
import curses
import time
stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
#curses.echo()            # Enable echoing of characters

offsets = ["a", "a", "a"]

stdscr.addstr(1, 0, ''.join(offsets))

stdscr.addstr(0, 0, "▲")
stdscr.addstr(2, 0, "▼")

stdscr.addstr(0, 1, "▲")
stdscr.addstr(2, 1, "▼")

stdscr.addstr(0, 2, "▲")
stdscr.addstr(2, 2, "▼")

stdscr.move(1, 0)
p = False
# Get a 15-character string, with the cursor on the top line
#s = stdscr.getstr(0,0,)
while True:
    c = stdscr.getch()
    if p:
        print(c)
    if c == curses.KEY_UP:
        pos = stdscr.getyx()
        offsets[pos[1]] = intToChar((charToInt(offsets[pos[1]])+1) % 26)
        stdscr.addstr(1, 0, ''.join(offsets))
        stdscr.move(pos[0], pos[1])
        stdscr.refresh()
    if c == curses.KEY_DOWN:
        pos = stdscr.getyx()
        offsets[pos[1]] = intToChar((charToInt(offsets[pos[1]])-1) % 26)
        stdscr.addstr(1, 0, ''.join(offsets))
        stdscr.move(pos[0], pos[1])
        stdscr.refresh()
    if c == curses.KEY_LEFT:
        if stdscr.getyx()[1] > 0:
            stdscr.move(stdscr.getyx()[0], stdscr.getyx()[1]-1)
            stdscr.refresh()

    if c == curses.KEY_RIGHT:
        if stdscr.getyx()[1] < 2:
            stdscr.move(stdscr.getyx()[0], stdscr.getyx()[1]+1)
            stdscr.refresh()
    if (c >= 97 and c <=122):
        pos = stdscr.getyx()
        offsets[stdscr.getyx()[1]] = intToChar(c-97)
        stdscr.addstr(1, 0, ''.join(offsets))
        stdscr.move(pos[0], pos[1])
        stdscr.refresh()
    if (c >= 65 and c <=90):
        pos = stdscr.getyx()
        offsets[stdscr.getyx()[1]] = intToChar(c-65)
        stdscr.addstr(1, 0, ''.join(offsets))
        stdscr.move(pos[0], pos[1])
        stdscr.refresh()
    if c == curses.KEY_ENTER or c == 10:
        break  # Exit the while loop
    if c == curses.KEY_BACKSPACE:
        if p:
            p = False
        elif not p:
            p = True



stdscr.refresh()



curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
print(''.join(offsets))