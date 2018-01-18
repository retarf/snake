from curses import wrapper
import curses


class Snake:

    def __init__(self, screen, pos_y, pos_x, length):
        self.screen = screen
        self.x = pos_x
        self.y = pos_y
        self.length = length
        self.speed = 50  # speed in ms
        self.direction = self.move_up
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

        if c == curses.KEY_UP:
            self.move_up()
            self.direction = self.move_up

        elif c == curses.KEY_DOWN:
            self.move_down()
            self.direction = self.move_down

        elif c == curses.KEY_RIGHT:
            self.move_right()
            self.direction = self.move_right

        elif c == curses.KEY_LEFT:
            self.move_left()
            self.direction = self.move_left

        elif c == -1:
            self.direction()



def main(screen):
    screen.clear()
    screen.nodelay(True)
    curses.curs_set(False)
    snake = Snake(screen, 25, 84, 30)
    while True:
        snake.show()
        snake.move()

        curses.napms(snake.speed)


wrapper(main)
