import os
import random
import threading

r = random.Random()


class Game:
    def __init__(self, timeout=3):
        self.timeout = timeout
        self.timer = threading.Timer(self.timeout, self.timer_stop)
        self.draw_new_number()
        self.is_game_on: bool = True
        self.timer.start()

    def draw_new_number(self):
        self.number = random.Random.randint(r, 1, 50)
        print("new number: ", self.number)

    def win(self):
        self.is_game_on = False
        self.timer.cancel()
        print("win, end of game!")

    def timer_stop(self):
        print("timeout!")
        self.new_round()

    def new_round(self):
        self.timer.cancel()
        self.timer = threading.Timer(self.timeout, self.timer_stop)
        self.draw_new_number()
        self.timer.start()

    def guess_the_number(self):
        while g.is_game_on is True:
            try:
                input_number = int(input())
                if self.number == input_number:
                    self.win()
                else:
                    print("miss")

            except ValueError:
                print("miss")


if __name__ == '__main__':
    g = Game()
    g.guess_the_number()
