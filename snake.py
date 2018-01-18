#!/bin/env python

from curses import wrapper
import curses


class Snake:

    def __init__(self, screen, pos_y=-1, pos_x=-1, length=3, speed=100):
        self.screen = screen
        (self.screen_y, self.screen_x) = screen.getmaxyx()
        self.x = pos_x
        if self.x == -1:
            self.x = int(self.screen_x/2)
        self.y = pos_y
        if self.y == -1:
            self.y = int(self.screen_y/2)
        self.length = length
        self.speed = speed  # speed in ms
        self.direction = self.move_right
        self.look = "@"
        self.body = []
        self.body.append((self.y, self.x))

    def move_left(self):
        '''Move left and append coordinate to body'''
        self.x -= 1
        self.body.append((self.y, self.x))

    def move_right(self):
        '''Move right and append coordinate to body'''
        self.x += 1
        self.body.append((self.y, self.x))

    def move_up(self):
        '''Move up and append coordinate to body'''
        self.y -= 1
        self.body.append((self.y, self.x))

    def move_down(self):
        '''Move down and append coordinate to body'''
        self.y += 1
        self.body.append((self.y, self.x))

    def last(self):
        '''Return coordinate of last pice of body'''
        if len(self.body) > self.length:
            last = self.body.pop(0)
            return last

    def show(self):
        '''Show snake on the screen'''
        self.screen.clear()

        last = self.last()
        # first delete last pice
        if last:
            (last_y, last_x) = last
            self.screen.delch(last_y, last_x)
        # then draw snake on the screen
        for pice in self.body:
            (pice_y, pice_x) = pice
            self.screen.addch(pice_y, pice_x, self.look)

        self.screen.refresh()

    def move(self):
        '''Move snake after sec second, takes keys to change direction'''
        c = self.screen.getch()
        curses.flushinp()
        print(self.direction)

        if c == curses.KEY_UP and self.direction != self.move_down:
            self.move_up()
            self.direction = self.move_up

        elif c == curses.KEY_DOWN and self.direction != self.move_up:
            self.move_down()
            self.direction = self.move_down

        elif c == curses.KEY_RIGHT and self.direction != self.move_left:
            self.move_right()
            self.direction = self.move_right

        elif c == curses.KEY_LEFT and self.direction != self.move_right:
            self.move_left()
            self.direction = self.move_left

        else:
            self.direction()

    def eat(self):
        pass



def main(screen):
    screen.clear()
    screen.nodelay(True)
    curses.curs_set(False)
    snake = Snake(screen)
    while True:
        snake.show()
        snake.move()

        curses.napms(snake.speed)


wrapper(main)
