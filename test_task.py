import sys


class WrongValue(Exception):
    ...


class Maze:

    steps = [
        [0, (0, 0)],
        [1, (1, 0)],
        [2, (2, 0)],
        [3, (2, -1)],
        [4, (1, -1)],
        [5, (1, -2)],
        [6, (2, -2)],
        [7, (3, -2)],
        [8, (4, -2)],
        [9, (5, -2)],
        [10, (5, -3)],
        [11, (5, -4)],
        [12, (6, -4)],
        [13, (7, -4)],
        [14, (8, -4)],
        [15, (9, -4)],
        [16, (9, -5)],
        [17, (8, -5)],
        [18, (8, -6)],
        [19, (8, -7)],
        [20, (7, -7)],
        [21, (7, -8)],
        [22, (8, -8)],
        [23, (8, -9)],
        [24, (9, -9)],
        [25, (10, -9)]
    ]

    walls = [
        [2, (1, -1)],
        [2, (1, 1)],
        [3, (2, 1)],
        [3, (3, 0)],
        [4, (3, -1)],
        [4, (2, -2)],
        [5, (1, 0)],
        [5, (0, -1)],
        [6, (0, -2)],
        [6, (1, -3)],
        [7, (2, -1)],
        [8, (3, -1)],
        [8, (3, -3)],
        [9, (4, -3)],
        [10, (6, -2)],
        [11, (6, -3)],
        [12, (5, -5)],
        [12, (4, -4)],
        [13, (6, -3)],
        [14, (7, -3)],
        [14, (7, -5)],
        [15, (8, -3)],
        [15, (8, -5)],
        [16, (9, -3)],
        [16, (10, -3)],
        [17, (10, -5)],
        [17, (9, -6)],
        [18, (7, -5)],
        [18, (8, -4)],
        [19, (7, -6)],
        [19, (8, -6)],
        [20, (9, -7)],
        [20, (8, -8)],
        [21, (7, -6)],
        [21, (6, -7)],
        [21, (7, -6)],
        [22, (7, -9)],
        [23, (8, -7)],
        [23, (9, -8)],
        [24, (7, -9)],
        [24, (8, -10)],
        [25, (9, -8)],
        [25, (9, -10)],
    ]
    wrong_ways = [
        [1, (0, 1)],
        [1, (0, -1)],
        [1, (-1, 0)],
        [7, (2, -3)],
        [9, (4, -1)],
        [10, (5, -1)],
        [11, (4, -3)],
        [13, (6, -5)],
        [19, (9, -6)],
        [22, (6, -8)],
    ]
    bone = [25, (10, -9)]


class Dog:
    paws = 4
    tail = 1
    count_steps = 0

    def __init__(self, name):
        self.name = name
        self.__x = 0
        self.__y = 0

    def step(self):
        if [self.count_steps, (self.__x, self.__y)] in Maze.steps:
            self.count_steps += 1
            print(f"{self.count_steps} {self.name}'s step:")
            direction = str(input("Direction(enter in small letters): "))
            if direction == "up":
                self.__y += 1
            elif direction == "down":
                self.__y -= 1
            elif direction == "right":
                self.__x += 1
            elif direction == "left":
                self.__x -= 1
            else:
                raise WrongValue("Wrong direction value!")
        elif [self.count_steps, (self.__x, self.__y)] in Maze.walls:
            print(f"{self.name} hit the wall, game is over :( \nTry again!")
            sys.exit()
        elif [self.count_steps, (self.__x, self.__y)] in Maze.wrong_ways:
            print(f"{self.name} chose a wrong way, game is over :( \nTry again!")
            sys.exit()
        else:
            print(f"{self.name}, you are a coward! \nTry again!")
            sys.exit()
        if [self.count_steps, (self.__x, self.__y)] == Maze.bone:
            print("YOU WIN!!!!!!")
            sys.exit()
        if [self.count_steps, (self.__x, self.__y)] in Maze.steps:
            print(f"{self.name} found the right way! ")


dog1 = Dog("Sharick")
for step in range(len(Maze.steps)):
    dog1.step()

# Все правильные шаги:
# 1) 'right'
# 2) 'right'
# 3) 'down'
# 4) 'left'
# 5) 'down'
# 6) 'right'
# 7) 'right'
# 8) 'right'
# 9) 'right'
# 10) 'down'
# 11) 'down'
# 12) 'right'
# 13) 'right'
# 14) 'right'
# 15) 'right'
# 16) 'down'
# 17) 'left'
# 18) 'down'
# 19) 'down'
# 20) 'left'
# 21) 'down'
# 22) 'right'
# 23) 'down'
# 24) 'right'
# 25) 'right'
