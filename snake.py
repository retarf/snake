from curses import wrapper
import curses


class Snake:

    def __init__(self, pos_y, pos_x, length):
        self.x = pos_x
        self.y = pos_y
        self.length = length
        self.look = "@"
        self.body = []

    # def move_dec(func):
    #     def move():
    #     screen.addch(snake.y, snake.x, snake.look)
    #     c = screen.getch()
    #     curses.flushinp()
    #     if c == curses.KEY_UP:
    #         snake.move_up()
    #     elif c == curses.KEY_DOWN:
    #         snake.move_down()
    #     elif c == curses.KEY_RIGHT:
    #         snake.move_right()
    #     elif c == curses.KEY_LEFT:
    #         snake.move_left()
    #     screen.refresh()

    #     curses.napms(100)

    def move_left(self):
        self.x -= 1
        self.body.append((self.y, self.x))

    def move_right(self):
        self.x += 1
        self.body.append((self.y, self.x))

    def move_up(self):
        self.y -= 1
        self.body.append((self.y, self.x))

    def move_down(self):
        self.y += 1
        self.body.append((self.y, self.x))

    def last(self):
        if len(self.body) == self.length - 1:
            last = self.body.pop(1)
            return self.body
        else:
            return None


def main(screen):
    screen.clear()
    screen.nodelay(True)
    curses.curs_set(False)
    snake = Snake(25, 84, 3)
    print(screen.getmaxyx())
    screen.addch(snake.y, snake.x, snake.look)
    while True:
        c = screen.getch()
        curses.flushinp()
        screen.addch(snake.y, snake.x, snake.look)
        # print(screen.getmaxyx())
        if c == curses.KEY_UP:
            snake.move_up()
        elif c == curses.KEY_DOWN:
            snake.move_down()
        elif c == curses.KEY_RIGHT:
            snake.move_right()
        elif c == curses.KEY_LEFT:
            snake.move_left()

        # print(snake.last())
        # if snake.last():
            # print(snake.last())
            # screen.addstr(1, 1, snake.body)
            # (last_y, last_x) = snake.last()
            # screen.delch(last_y, last_x)

        screen.refresh()

        curses.napms(50)


wrapper(main)
