#!/bin/env python

import curses

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

    y_question = 'Podaj wielkość planszy Y: '
    x_question = 'Podaj wielkość planszy X: '
    mode_question = 'Podaj tryb gry Free / Cage: '

    start = get_center(4, len(mode_question) + 5)
    
    win = curses.newwin(7, len(mode_question) + 5, start[0], start[1])
    
    win.clear()
    win.border()

    win.addstr(1, 1, y_question)
    win.addstr(2, 1, x_question)
    win.addstr(3, 1, mode_question)
    win.addstr(4, 1, str(curses.COLS))
    win.addstr(5, 1, str(max_x))
    
    win.refresh()
    
    win.getch()
    
    curses.noecho()
    win.clear()
    win.refresh()
    
    del win

