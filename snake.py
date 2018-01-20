#!/bin/env python

from curses import wrapper
import curses
import sys
from random import randrange

class Snake:

    def __init__(self, screen, pos_y=-1, pos_x=-1, length=3, speed=100):
        self.screen = screen
        (self.screen_y, self.screen_x) = screen.getmaxyx()
        self.x = pos_x
        if self.x == -1:
            self.x = int(self.screen_x / 2)
        self.y = pos_y
        if self.y == -1:
            self.y = int(self.screen_y / 2)
        self.pos = (self.y, self.x)
        self.length = length
        self.speed = speed  # speed in ms
        self.direction = self.move_right
        self.look = "@"
        self.body = []
        self.body.append((self.y, self.x))

    # # def move_left(self):
    ##     '''Move left and append coordinate to body'''
    #     self.x -= 1
    #     self.body.append((self.y, self.x))

    # # def move_right(self):
    #     '''Move right and append coordinate to body'''
    #     self.x += 1
    #     self.body.append((self.y, self.x))

    # # def move_up(self):
    #     '''Move up and append coordinate to body'''
    #     self.y -= 1
    #     self.body.append((self.y, self.x))

    # def move_down(self):
    #     '''Move down and append coordinate to body'''
    #     self.y += 1
    #     self.body.append((self.y, self.x))

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
    
    def eat(self):
        pass

    def body_check(self):
        '''Check if snake eat him self'''
        # check if snake dont eat him self
        if self.body.count(self.pos) > 1:
            print('Game over')
            curses.napms(2000)
            sys.exit(1)


class FreeSnake(Snake):
    '''This snake will go through the walls'''

    def __init__(self, screen, pos_y=-1, pos_x=-1, length=3, speed=100):
        super().__init__(screen, pos_y, pos_x, length, speed)
        self.max_x = self.screen.getmaxyx()[1] - 1
        self.max_y = self.screen.getmaxyx()[0] - 1

    def move_left(self):
        '''Move left and append coordinate to body'''
        self.x -= 1
        if self.x < 0:
            self.x = self.max_x
        self.body.append((self.y, self.x))

    def move_right(self):
        '''Move right and append coordinate to body'''
        self.x += 1
        if self.x > self.max_x:
            self.x = 0
        self.body.append((self.y, self.x))

    def move_up(self):
        '''Move up and append coordinate to body'''
        self.y -= 1
        if self.y < 0:
            self.y = self.max_y
        self.body.append((self.y, self.x))

    def move_down(self):
        '''Move down and append coordinate to body'''
        self.y += 1
        if self.y > self.max_y:
            self.y = 0
        self.body.append((self.y, self.x))


class CageSnake(Snake):
    '''This snake won't go through the walls'''

    def __init__(self, screen, pos_y=-1, pos_x=-1, length=3, speed=100):
        super().__init__(screen, pos_y, pos_x, length, speed)
        self.max_x = self.screen.getmaxyx()[1] - 1
        self.max_y = self.screen.getmaxyx()[0] - 1

    def move_left(self):
        '''Move left and append coordinate to body'''
        self.x -= 1
        if self.x < 0:
            self.game_over()
        else:
            self.body.append((self.y, self.x))

    def move_right(self):
        '''Move right and append coordinate to body'''
        self.x += 1
        if self.x > self.max_x:
            self.game_over()
        else:
            self.body.append((self.y, self.x))

    def move_up(self):
        '''Move up and append coordinate to body'''
        self.y -= 1
        if self.y < 0:
            self.game_over()
        else:
            self.body.append((self.y, self.x))

    def move_down(self):
        '''Move down and append coordinate to body'''
        self.y += 1
        if self.y > self.max_y:
            self.game_over()
        else:
            self.body.append((self.y, self.x))

    def game_over(self):
        ''' Temporary function. Show Game over when snake touch the wall'''
        self.screen.clear()
        self.screen.addstr(10, 10, "Game over")
        self.screen.refresh()
        curses.napms(2000)
        sys.exit(1)


class Meal:
    ''' Generate and show snake snaks '''
    from random import randrange

    def __init__(self, screen, number):
        self.screen = screen
        self.number = number
        self.size_y = screen.getmaxyx()[0] - 1
        self.size_x = screen.getmaxyx()[1] - 1
        full_scr = self.size_y * self.size_x 
        if self.number > full_scr: 
            raise ToManySnacks
        self.snacks = []
        self.look = "o"

    def generate(self):
        ''' Generate snack fields '''
        while len(self.snacks) < self.number:
            y = randrange(1, self.size_y)
            x = randrange(1, self.size_x)
            if self.snacks.count((y, x)) == 0:
                self.snacks.append((y, x))

    def show(self):
        ''' Show snacks on the screen '''
        for snack in self.snacks:
            (y, x) = snack
            self.screen.addch(y, x, self.look)


class Board:

    def __init__(self, screen, size_y=1, size_x=1, mode="free"):
        self.screen = screen
        self.size_y = size_y
        self.size_x = size_x
        # Check mode and make snake
        if mode == "free":
            self.snake = FreeSnake(self.screen, length=3, speed=100)
        elif mode == "cage":
            self.snake = CageSnake(self.screen, length=3, speed=100)
        else:
            raise SnakeError('Something with snake object creation')

    def show_snake(self):
        self.snake.move()
        self.snake.body_check()
        self.snake.show()

    def show_snacks(self):
        pass



def main(screen):
    screen.clear()
    screen.nodelay(True)
    curses.curs_set(False)
    # screen.resize(30, 30)
    snake = FreeSnake(screen, length=100, speed=50)
    # scr = curses.newwin(10, 10, 40, 5)
    meal = Meal(screen, 10)
    while True:
        meal.generate()
        meal.show()
        
        # print(screen.getmaxyx())
        # print(snake.pos)

        screen.border('#', '#', '#', '#', '#', '#', '#', '#')
        screen.refresh()
        curses.napms(snake.speed)

wrapper(main)
