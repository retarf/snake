#!/bin/env python

from curses import wrapper
import curses
from game_over import game_over

class Snake:

    def __init__(self, screen, pos_y=-1, pos_x=-1, length=3, speed=100):
        self.screen = screen
        self.min_y = 1 
        self.min_x = 1 
        self.max_y = self.screen.getmaxyx()[0] - 2
        self.max_x = self.screen.getmaxyx()[1] - 2
        self.x = pos_x
        self.y = pos_y
        if self.x == -1:
            self.x = int(self.max_x / 2)
        if self.y == -1:
            self.y = int(self.max_y / 2)
        self.pos = (self.y, self.x)
        self.length = length
        self.first_length = length
        self.last = None
        self.speed = speed  # speed in ms
        self.direction = self.move_right
        self.look = "@"
        self.body = []
        self.body.append((self.y, self.x))
        self.score = 0

    def last_pos(self):
        '''Return coordinate of last pice of body'''
        if len(self.body) > self.length:
            last = self.body.pop(0)
            self.last = last

    def show(self):
        '''Show snake on the screen'''

        curses.init_pair(1, 1, 0)
        # self.last_pos()

        last = self.last
        # first delete last pice
        if last:
            (last_y, last_x) = last
            # delete last element
            self.screen.addch(last_y, last_x, ' ')
        # then draw snake on the screen
        for pice in self.body:
            (pice_y, pice_x) = pice
            self.screen.addstr(pice_y, pice_x, self.look, curses.color_pair(1))

    def move(self):
        '''Move snake after sec second, takes keys to change direction and save first element actual position'''
        c = self.screen.getch()
        curses.flushinp()

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

        # save first element position
        self.pos = self.body[len(self.body) - 1]
        self.last_pos()

    def eat(self, snack):
        ''' Snake eat meal.snacks '''
        if self.pos == snack: 
            self.length += 1
            self.score += 1
            if self.length > (self.max_y * self.max_x):
                self.show()
                self.screen.refresh()
                game_over(self.screen, self.score)
        

    def body_check(self):
        '''Check if snake eat him self'''
        if self.body.count(self.pos) > 1:
            game_over(self.screen, self.score)

class FreeSnake(Snake):
    '''This snake will go through the walls'''

    def move_left(self):
        '''Move left and append coordinate to body'''
        self.x -= 1
        if self.x < self.min_x:
            self.x = self.max_x
        self.body.append((self.y, self.x))

    def move_right(self):
        '''Move right and append coordinate to body'''
        self.x += 1
        if self.x > self.max_x:
            self.x = self.min_x 
        self.body.append((self.y, self.x))

    def move_up(self):
        '''Move up and append coordinate to body'''
        self.y -= 1
        if self.y < self.min_y:
            self.y = self.max_y
        self.body.append((self.y, self.x))

    def move_down(self):
        '''Move down and append coordinate to body'''
        self.y += 1
        if self.y > self.max_y:
            self.y = self.min_y
        self.body.append((self.y, self.x))


class CageSnake(Snake):
    '''This snake won't go through the walls'''

    def move_left(self):
        '''Move left and append coordinate to body'''
        self.x -= 1
        if self.x < 1:
            game_over(self.screen, self.score)
        else:
            self.body.append((self.y, self.x))

    def move_right(self):
        '''Move right and append coordinate to body'''
        self.x += 1
        if self.x > self.max_x:
            game_over(self.screen, self.score)
        else:
            self.body.append((self.y, self.x))

    def move_up(self):
        '''Move up and append coordinate to body'''
        self.y -= 1
        if self.y < 1:
            game_over(self.screen, self.score)
        else:
            self.body.append((self.y, self.x))

    def move_down(self):
        '''Move down and append coordinate to body'''
        self.y += 1
        if self.y > self.max_y:
            game_over(self.screen, self.score)
        else:
            self.body.append((self.y, self.x))
