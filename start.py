#!/bin/env python

import curses

def value_error():
    line1 = "Podales zla wartosc!!!"
    line2 = "Sprobuj ponownie!"
    
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.curs_set(False)
    
    begin = int((curses.COLS - len(line1)) / 2)
    
    s = curses.newwin(4, len(line1) + 4, 3, begin)
    s.clear()
    s.border()
    s.addstr(1, 2, line1, curses.color_pair(1))
    s.addstr(2, 2, line2, curses.color_pair(1))
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
    mode = "Free"

    y_question = 'Podaj wielkość planszy Y: '
    x_question = 'Podaj wielkość planszy X: '
    mode_question = 'Podaj tryb gry Free / Cage: '

    start = get_center(4, len(mode_question) + 20)
    
    win = curses.newwin(7, len(mode_question) + 20, start[0], start[1])

    while True:
    
        win.clear()
        win.border()

        win.addstr(1, 1, y_question)
        win.addstr(2, 1, x_question)
        win.addstr(3, 1, mode_question)
        win.addstr(5, 1, str(curses.getsyx()))
        
        win.refresh()
        
    
        try:
            y = int(win.getstr(1, len(y_question) + 2, 3))
            x = int(win.getstr(2, len(x_question) + 2, 2))
            mode = win.getstr(3, len(mode_question) + 2, 4)
            if mode != "Free" or mode != "Cage":
                raise ValueError
            break
        except ValueError:
            value_error()

        win.addstr(4, 1, mode)
        win.addstr(5, 1, str(y))
        win.refresh()
        curses.napms(2000)
    
    curses.noecho()
    win.clear()
    win.refresh()
    
    del win

    return (y, x, mode)

