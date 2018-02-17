from gym import Env, spaces
from models import Snake, Reward
import pygame, sys
import numpy as np

class SnakeEnv(Env):

    metadata = {'render.modes': ['human']}

    def __init__(self, fps=10, size=20, unit=10, render=True):
        """
        Screen size: size * unit px
        """
        self.fps = fps
        self.size = size
        self.unit = unit
        self.shouldRender = render
        if self.shouldRender:
            pygame.init()
            self.screen = pygame.display.set_mode((size * unit, size * unit))
            self.clock = pygame.time.Clock()

        self.screenColor = (0, 0, 0)
        self.snakeColor = (255, 255, 255)
        self.rewardColor = (255, 0, 0)

        self.done = False
        self.snake = None
        self.reward = None
        self.winReward = 100
        self.loseReward = -100
        self.dotReward = 1

        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Box(low=0, high=2, shape=(size,size))

    def reset(self):
        """
        Returns initial observation
        """
        self.done = False
        mid = self.size // 2
        # starts at midpoint
        self.snake = Snake(self.size, mid, mid)
        self.reward = Reward(self.size, self.snake.body)

        obs = np.zeros((self.size, self.size), dtype=int)
        if not self.snake.isDead():
            for x, y, _ in self.snake.body:
                obs[x][y] = 1
        obs[self.reward.x][self.reward.y] = 2

        return obs

    def step(self, action):
        """
        action (int): a number from 0 to 4, denoting None, Up, Down, Left, Right respectively.

        Returns:
        observation (object): ...
        reward (float): ...
        done (boolean): has the episode terminated?
        info (dict): diagnostic information useful for debugging.
        """
        if self.done:
            raise Exception("Environment has already finished. Call reset()!")
        if action not in range(5):
            raise Exception("Action must be from 0 to 4.")

        points = 0
        self.snake.changeDir(action)
        self.snake.move()

        # Got a reward
        if self.snake.head[0] == self.reward.x and self.snake.head[1] == self.reward.y:
            self.snake.grow()
            points += self.dotReward
            # Beat the game
            if self.snake.length == self.size * self.size:
                points += self.winReward
                self.done = True
            else:
                self.reward = Reward(self.size, self.snake.body)

        if self.snake.isDead():
            points += self.loseReward
            self.done = True

        # Update state
        obs = np.zeros((self.size, self.size), dtype=int)
        if not self.snake.isDead():
            for x, y, _ in self.snake.body:
                obs[x][y] = 1
        obs[self.reward.x][self.reward.y] = 2
        info = None

        return (obs, points, self.done, info)

    def render(self, mode='human'):
        if mode == 'human':
            if not self.shouldRender:
                raise Exception("You must initialize the environment with render set to true.")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.screenColor)

            for x, y, _ in self.snake.body:
                snake_block = pygame.Rect(x * self.unit, y * self.unit, self.unit, self.unit)
                pygame.draw.rect(self.screen, self.snakeColor, snake_block)

            reward_block = pygame.Rect(self.reward.x * self.unit, self.reward.y * self.unit, self.unit, self.unit)
            pygame.draw.rect(self.screen, self.rewardColor, reward_block)

            pygame.display.flip()
            self.clock.tick(self.fps)
        else:
            super(SnakeEnv, self).render(mode=mode)

    def close(self):
        print('Closing...')

    def interactive(self):
        """
        Time to play!
        """
        if not self.shouldRender:
            raise Exception("You must initialize the environment with render set to true.")

        self.reset()
        while not self.done:
            action = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        action = 1
                    elif event.key == pygame.K_DOWN:
                        action = 2
                    elif event.key == pygame.K_LEFT:
                        action = 3
                    elif event.key == pygame.K_RIGHT:
                        action = 4
            _, _, self.done, _ = self.step(action)
            if self.done:
                break
            self.render()
