#!/bin/env python

from curses import wrapper
import curses
import sys
from random import randrange

class Board:

    def __init__(self, screen, size_y=1, size_x=1, mode="free"):
        self.screen = screen
        self.size_y = size_y
        self.size_x = size_x

    def show_snake(self):
        ''' Main function to show snake on the screen '''
       
        # Check mode and make snake
        if self.mode == "free":
            self.snake = FreeSnake(self.screen, length=3, speed=100)
        elif mode == "cage":
            self.snake = CageSnake(self.screen, length=3, speed=100)
        else:
            raise SnakeError('Something with snake object creation')

        self.snake.move()
        self.snake.body_check()
        self.snake.eat(self.meal)
        self.snake.show()

    def show_snacks(self):
        
        ''' Show snacks on the screen '''
        for snack in meal.snacks:
            (y, x) = snack
            self.screen.addch(y, x, meal.look)

    def show(self, snake, meal):

        '''Show snake on the screen'''
        last = snake.last()
        # first delete last pice
        if last:
            (last_y, last_x) = last
            # self.screen.delch(last_y, last_x)
            self.screen.addch(last_y, last_x, ' ')
        # then draw snake on the screen
        for pice in snake.body:
            (pice_y, pice_x) = pice
            self.screen.addch(pice_y, pice_x, snake.look)



        # self.screen.border('#', '#', '#', '#', '#', '#', '#', '#')

def main(screen):
    screen.clear()
    screen.nodelay(True)
    curses.curs_set(False)
    # screen.resize(30, 30)
    snake = FreeSnake(screen, length=10, speed=150)
    # scr = curses.newwin(10, 10, 40, 5)
    meal = Meal(screen, 10)
    meal.generate()
    board = Board(screen)
    while True:
        board.show(snake, meal)
        
        # print(screen.getmaxyx())
        # print(snake.pos)

        screen.refresh()
        curses.napms(snake.speed)

wrapper(main)
