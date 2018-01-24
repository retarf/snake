#!/bin/env python

from curses import wrapper
import curses

from snake import CageSnake, FreeSnake
from meal import Meal

from start import menu
from game_over import game_over


def main(screen):
    
    # Choose window size and mode
    (y, x, mode) = menu()

    max_y = curses.LINES - 1
    max_x = curses.COLS - 1

    screen.clear()
    screen.nodelay(True)
    screen.resize(y, x)
    curses.curs_set(False)

    speed = 1500

    if mode == "free":
        snake = FreeSnake(screen, length=3, speed=speed)
    elif mode == "cage":
        snake = CageSnake(screen, length=3, speed=speed)

    score_win = curses.newwin(1, 22, max_y, int((max_x - 11) / 2))
    meal = Meal(screen)
    meal.generate(snake.body)

    while True:
        screen.clear()
        snake.move()
        snake.body_check()
        # if snake ate
        if snake.pos == meal.pos:
            snake.eat(meal.pos)
            meal.generate(snake.body)
        snake.show()
        meal.show()

        # add border
        screen.border('#', '#', '#', '#', '#', '#', '#', '#',) 
        screen.refresh()
        
        score = "o: " + str(snake.score) + "  max: " + str((meal.max_y - 1) * (meal.max_x - 1) - snake.first_length)
        score_win.addstr(0, 0, score, curses.color_pair(2))
        score_win.refresh()
        screen.refresh()
        curses.napms(snake.speed)

wrapper(main)
