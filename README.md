# Snake for Gym

Snake environment for OpenAI Gym, written in Python 3.

## Dependencies

* [Gym](https://github.com/openai/gym)
* [Pygame](https://www.pygame.org)

Run it like a Gym environment:

```python
from snake import SnakeEnv

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

SnakeEnv takes in 5 parameters.

1. Size: the game is composed of nxn blocks, and size specifies n.
2. Reward: reward for eating a dot/fruit.
3. Win: reward for winning (no more space in the map).
4. Lose: reward for losing.
5. FPS: frames per second (for rendering).
6. Unit: specifies how big each block is (for rendering).

Default: fps=10, size=20, unit=10, reward=1, win=10, lose=-1

## Actions

0: Keep the current direction

1: Up

2: Down

3: Left

4: Right

## Observation

Returns an nxn numpy array.

* Empty blocks are represented by 0's
* Snake body is represented by 1's
* The reward is represented by 2.

## Alternatives

[PyGame Learning Environment](http://pygame-learning-environment.readthedocs.io/) also has a snake environment with other games as well.

[YuriyGuts's snake for AI](https://github.com/YuriyGuts/snake-ai-reinforcement) has examples and GPU support.

