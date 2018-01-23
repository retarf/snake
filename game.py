#!/bin/env python

from curses import wrapper
import curses

from snake import CageSnake, FreeSnake
from meal import Meal

from startend import menu


def main(screen):
    
    # screen = curses.newwin(0, 0)
    # screen.keypad(True)
    
    (y, x, mode) = menu()

    max_y = curses.LINES - 1
    max_x = curses.COLS - 1

    screen.clear()
    screen.nodelay(True)
    screen.resize(y, x)
    # screen.resize(max_y - 1, max_x)
    screen.clear()
    screen.border()
    
    curses.curs_set(False)
    if mode == "Free":
        snake = FreeSnake(screen, length=3, speed=100)
    elif mode == "Cage":
        snake = CageSnake(screen, length=3, speed=100)
    score_win = curses.newwin(1, 10, max_y, int((max_x - 11) / 2))
    meal = Meal(screen)
    meal.generate(snake.body)
    while True:
        screen.clear()
        snake.move()
        snake.body_check()
        if snake.pos == meal.pos:
            snake.eat(meal.pos)
            meal.generate(snake.body)
        meal.show()
        snake.show()

        # add border

        screen.border('#', '#', '#', '#', '#', '#', '#', '#',) 
        

        score = "o: " + str(snake.score)
        score_win.addstr(0, 0, score, curses.color_pair(2))
        score_win.refresh()
        screen.refresh()
        curses.napms(snake.speed)

wrapper(main)
