#!/bin/env python

import curses

def choose_mode(win, len_q):

    mode = "free"
    
    win.addstr(3, len_q, "Free", curses.A_REVERSE)
    win.addstr(3, len_q + 4, " / Cage", curses.A_NORMAL)
    win.refresh()

    curses.curs_set(False)
    curses.noecho()
    win.keypad(True)

    while True: 

        c = win.getch()

        if c == curses.KEY_LEFT:
            win.addstr(3, len_q, "Free", curses.A_REVERSE)
            win.addstr(3, len_q + 4, " / Cage", curses.A_NORMAL)
            
            mode = "free"

        elif c == curses.KEY_RIGHT:
            win.addstr(3, len_q, "Free / ", curses.A_NORMAL)
            win.addstr(3, len_q + 7, "Cage", curses.A_REVERSE)

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

    # windows size
    x_size = len(max(args, key=len)) + 2
    y_size = len(args) + 2

    
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(False)
    
    begin = int((curses.COLS - x_size) / 2)
    
    s = curses.newwin(y_size, x_size + 2, 3, begin)
    s.clear()
    s.border()
    line = 0
    for arg in args:
        line += 1
        s.addstr(line, 2, arg, curses.color_pair(1))
    s.refresh()

    curses.napms(1500)
    s.clear()
    s.refresh()

    del s

    curses.curs_set(True)


def get_center(lines_number, length):
    max_y = curses.LINES - 1
    max_x = curses.COLS - 1

    y = int((max_y - lines_number) / 2)
    x = int((max_x - length) / 2)

    return (y, x)

def menu():

    curses.echo()

    max_y = curses.LINES - 1
    max_x = curses.COLS - 1

    y = max_y
    x = max_x
    mode = "free"

    y_question = 'Podaj wielkość planszy Y: '
    x_question = 'Podaj wielkość planszy X: '
    mode_question = 'Podaj tryb gry: '

    start = get_center(4, len(y_question) + 20)
    
    win = curses.newwin(7, len(y_question) + 20, start[0], start[1])

    while True:
    
        win.clear()
        win.border()

        win.addstr(1, 1, y_question)
        win.addstr(2, 1, x_question)
        win.addstr(3, 1, mode_question)
        win.addstr(5, 1, str(curses.getsyx()))
        
        win.refresh()
        
        len_q = len(mode_question) + 2
        
        try:
            y = int(win.getstr(1, len(y_question) + 2, 3))
            x = int(win.getstr(2, len(x_question) + 2, 2))
            mode = choose_mode(win, len_q)
            break
        except ValueError:
            value_error("Podales zla wartosc!!!", "Sprobuj ponownie!")
    
    curses.noecho()
    win.clear()
    win.refresh()
    
    del win

    return (y, x, mode)

