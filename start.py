#!/bin/env python

import curses

def choose_mode(win, len_q):
    ''' Function generate switch like menu '''

    mode = "free"
    
    # First look
    win.addstr(3, len_q, "Tak", curses.A_REVERSE)
    win.addstr(3, len_q + 3, " / Nie", curses.A_NORMAL)
    win.refresh()

    curses.curs_set(False)
    curses.noecho()
    win.keypad(True)

    # Switch if user press arrow button
    while True: 

        c = win.getch()

        if c == curses.KEY_LEFT:
            win.addstr(3, len_q, "Tak", curses.A_REVERSE)
            win.addstr(3, len_q + 3, " / Nie", curses.A_NORMAL)
            
            mode = "free"

        elif c == curses.KEY_RIGHT:
            win.addstr(3, len_q, "Tak / ", curses.A_NORMAL)
            win.addstr(3, len_q + 6, "Nie", curses.A_REVERSE)

            mode = "cage"
        
        elif c == 10 or c == 13 or curses.KEY_ENTER:
            break

        win.refresh()

    curses.curs_set(True)
    curses.echo()
    win.keypad(False)

    return mode

def value_error(*args):
    ''' Print value_error messages '''

    # windows size: length of max fraze from args + 4
    x_size = len(max(args, key=len)) + 4 
    y_size = len(args) + 2

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(False)
    
    begin = int((curses.COLS - x_size) / 2)
    
    win = curses.newwin(y_size, x_size + 2, 3, begin)
    win.clear()
    win.border()
    line = 0
    # print all messages line by line
    for arg in args:
        line += 1
        center = int((x_size - len(arg)) / 2)
        win.addstr(line, center, arg, curses.color_pair(1))

    win.refresh()
    curses.napms(1500)
    win.clear()
    win.refresh()
    del win
    curses.curs_set(True)


def get_center(lines_number, length):
    ''' Return start coordinates of center window ''' 
    max_y = curses.LINES - 1
    max_x = curses.COLS 

    y = int((max_y - lines_number) / 2)
    x = int((max_x - length) / 2)

    return (y, x)

def menu():

    curses.echo()

    max_y = curses.LINES - 1
    max_x = curses.COLS

    y = max_y
    x = max_x
    mode = "free"

    y_question = 'Podaj wielkość planszy Y: '
    x_question = 'Podaj wielkość planszy X: '
    mode_question = 'Przechodzenie przez ściany: '

    start = get_center(4, len(mode_question) + 13)
   
    # add SNAKE at the top of window
    win = curses.newwin(5, len(mode_question) + 13, start[0], start[1])
    word_snake = ' SNAKE '
    snake_len = len(word_snake)
    center = int((len(mode_question) + 13 - snake_len) / 2) 

    while True:
    
        win.clear()
        win.border()

        # add question strings 
        win.addstr(0, center, word_snake) 
        win.addstr(1, 1, y_question)
        win.addstr(2, 1, x_question)
        win.addstr(3, 1, mode_question)
        
        win.refresh()
        
        len_q = len(mode_question) + 2
        
        # get answers
        try:
            y = int(win.getstr(1, len(y_question) + 2, 3))
            if y < 5:
                value_error("Za mała plansza", "Minimalna wartość to:", "5")
                continue
            if y > max_y:
                value_error("Za duża plansza", "Maksymalna wartość to:", str(max_y))
                continue
            x = int(win.getstr(2, len(x_question) + 2, 3))
            if x < 5:
                value_error("Za mała plansza", "Minimalna wartość to:", "5")
                continue
            if x > max_x:
                value_error("Za duża plansza", "Maksymalna wartość to:", str(max_x))
                continue

            # choose mode using choose_mode()
            mode = choose_mode(win, len_q)
            # if everything is ok leave loop
            break
        except ValueError:
            value_error("Podales zla wartosc!!!", "Sprobuj ponownie!")
    
    curses.noecho()
    win.clear()
    win.refresh()
    
    del win

    return (y, x, mode)

