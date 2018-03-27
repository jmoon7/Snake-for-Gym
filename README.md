# Snake for Gym

Snake environment for OpenAI Gym, written in Python 3.

## Dependencies

* [Gym](https://github.com/openai/gym)
* [Pygame](https://www.pygame.org)

Run it like a Gym environment:

```python
from snake.env import SnakeEnv

env = SnakeEnv()

for episode in range(10):
    observation = env.reset()
    while True:
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
```

Play with it yourself!

```python
env = SnakeEnv()
env.interactive()
```

## SnakeEnv

Initialization parameters

1. state_size: the game is composed of nxn blocks, and size specifies n.
2. snake_size: size of the snake
3. reward_eat: reward for eating a dot/fruit.
4. reward_win: reward for winning (max score).
5. reward_lose: reward for losing.
6. reward_time: time discount reward
7. fps: frames per second (for rendering).
8. unit: specifies how big each block is (for rendering).

Default: state_size=20, snake_size=3, reward_eat=1, reward_win=10, reward_lose=-1, reward_time=-0.01, fps=10, unit=10

By default the snake starts at the midpoint and goes upwards.

## Actions

0: Do nothing

1: Up

2: Down

3: Left

4: Right

## Observation

Returns an nxn numpy array.

* Empty blocks are represented by 0's
* Snake body is represented by 1's
* The reward is represented by 2.

## Info

env.step also returns a dictionary named 'info'.

If the game has ended, (i.e. done == True), then you can inspect info

```python
if done: print(info['cause of death'])
```

To examine the cause of death. It takes on one of two string values: 'out of bounds' or 'self collision'.

## Alternatives

[PyGame Learning Environment](http://pygame-learning-environment.readthedocs.io/) also has a snake environment with other games as well.

[YuriyGuts's snake for AI](https://github.com/YuriyGuts/snake-ai-reinforcement) has examples and GPU support.
