#!/bin/env python

from curses import wrapper
import curses
import sys
from random import randrange

class Meal:
    ''' Generate and show snake snak '''

    def __init__(self, screen):
        self.screen = screen
        self.max_y = self.screen.getmaxyx()[0] - 1
        self.max_x = self.screen.getmaxyx()[1] - 1
        self.y = 2
        self.x = 2
        self.look = 'o'

    def generate(self, body):
        ''' Generate snack fields '''
        while True:
            self.y = randrange(1, self.max_y)
            self.x = randrange(1, self.max_x)
            self.pos = (self.y, self.x)
            if body.count(self.pos) == 0:
                break

    def show(self):
        ''' Show snack on the screen '''

        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.screen.addstr(self.y, self.x, self.look, curses.color_pair(2))
    
def main(screen):
    screen.clear()
    screen.nodelay(True)
    curses.curs_set(False)
    global max_y
    global max_x
    max_y = screen.getmaxyx()[0] - 2
    max_x = screen.getmaxyx()[1] - 2
    meal = Meal()
    meal.generate()
    while True:
        screen.clear()
        meal.show(screen)
        
        screen.refresh()
        curses.napms(100)

if __name__ == '__main__':
    wrapper(main)
