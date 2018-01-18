from curses import wrapper
import curses


class Snake:

    def __init__(self, screen, pos_y, pos_x, length):
        self.screen = screen
        self.x = pos_x
        self.y = pos_y
        self.length = length
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
        if len(self.body) == self.length:
            last = self.body.pop(1)
            return last
    
    def show(self):
        '''Show snake on the screen'''
        self.screen.clear()
        for pice in self.body:
            (pice_y, pice_x) = pice
            self.screen.addch(pice_y, pice_x, self.look)
        last = self.last()
        if last:
            (last_y, last_x) = last
            self.screen.delch(last_y, last_x)
        self.screen.refresh()


def main(screen):
    screen.clear()
    screen.nodelay(True)
    curses.curs_set(False)
    snake = Snake(screen, 25, 84, 3)
    while True:
        snake.show()
        c = screen.getch()
        curses.flushinp()
        if c == curses.KEY_UP:
            snake.move_up()
        elif c == curses.KEY_DOWN:
            snake.move_down()
        elif c == curses.KEY_RIGHT:
            snake.move_right()
        elif c == curses.KEY_LEFT:
            snake.move_left()



        curses.napms(50)


wrapper(main)
