import curses
import sys

def game_over(scr, score):
    ''' Display "Game over" '''

    scr.clear()
    scr.refresh()

    max_y = curses.LINES  
    max_x = curses.COLS 

    words = "Game over"
    score = "Score: " + str(score) 

    x_size = len(max((words, score), key=len)) + 20 
    y_size = 8 

    center = int((max_x - x_size) / 2)

    win = curses.newwin(y_size, x_size, 3, center)
    win.border()
    
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    center = int((x_size - len(words)) / 2)
    win.addstr(3, center, words, curses.color_pair(2))
    center = int((x_size - len(score)) / 2)
    win.addstr(4, center, score, curses.color_pair(1))

    scr.resize(max_y, max_x)

    text = 'Naciśnij ENTER'
    scr.addstr(int(max_y / 2),int((max_x - len(text)) / 2), text) 
    scr.refresh()
    win.refresh()
    
    # wait until user push ENTER button
    while True:
        c = win.getch()
        if c == curses.KEY_ENTER or c == 13 or c == 10:
            break

    scr.clear()
    scr.refresh()
    win.clear()
    win.refresh()

    curses.nocbreak()
    del win
    del scr
    sys.exit(1)
