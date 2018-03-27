import pygame, sys, random

class Snake:
    def __init__(self, size, x, y, length, dir):
        """
        size: size of the screen
        x,y: inital position
        dir: initial direction
        length: inital length
        """
        self.size = size
        self.dir = dir
        self.length = length
        self.body = None
        if dir == 1:
            self.body = [[x, y+i, dir] for i in range(length)]
        elif dir == 2:
            self.body = [[x, y-i, dir] for i in range(length)]
        elif dir == 3:
            self.body = [[x+i, y, dir] for i in range(length)]
        elif dir == 4:
            self.body = [[x-i, y, dir] for i in range(length)]
        self.head = self.body[0]

    def changeDir(self, d):
        if d in (1, 2) and self.dir in (3, 4) \
            or d in (3, 4) and self.dir in (1, 2):
            self.dir = d

    def move(self):
        d = self.dir
        for i in range(len(self.body)):
            # Up
            if d == 1:
                self.body[i][1] -= 1
            # Down
            elif d == 2:
                self.body[i][1] += 1
            # Left
            elif d == 3:
                self.body[i][0] -= 1
            # Right
            elif d == 4:
                self.body[i][0] += 1

            temp = self.body[i][2]
            self.body[i][2] = d
            d = temp

    def grow(self):
        x, y, d = self.body[-1]
        if d == 1:
            y += 1
        elif d == 2:
            y -= 1
        elif d == 3:
            x += 1
        elif d == 4:
            x -= 1
        self.body.append([x, y, d])
        self.length += 1

    def isDead(self):
        outOfBound = self.head[0] < 0 or self.head[0] >= self.size or \
                        self.head[1] < 0 or self.head[1] >= self.size
        selfCollision = False
        for x, y, _ in self.body[1:]:
            if self.head[0] == x and self.head[1] == y:
                selfCollision = True
        return (outOfBound, selfCollision)

class Reward:
    def __init__(self, size, blocked):
        self.x = random.randrange(size)
        self.y = random.randrange(size)

        # If reward spawned on snake's body
        while (self.x, self.y) in [(x[0], x[1]) for x in blocked]:
            self.x = random.randrange(size)
            self.y = random.randrange(size)
