def game_over(scr, score):
    ''' Display "Game over" '''

    scr.clear()
    scr.refresh()

    max_y = curses.LINES - 1
    max_x = curses.COLS - 1

    words = "Game over"
    score = "Score: " + str(score) 

    y_size = len(max((words, score), key=len))
    x_size = 2

    center = int((max_y - y_size) / 2)

    win = curses.newwin(y_size, x_size, 3, center)
    
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    win.addstr(1, 2, words, curses.color_pair(2))
    win.addstr(2, 2, score, curses.color_pair(2))

    curses.napms(2000)
