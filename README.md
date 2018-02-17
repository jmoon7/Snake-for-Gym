# Snake
Snake environment for OpenAI Gym, written in Python 3.

### Dependencies

* Gym
  > pip3 install gym

* Pygame
  > pip3 install pygame


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


Note: If you don't want to render your environment, in addition to not calling <code>env.render()</code>,
it's best to initialize with render set to False.
```python
env = SnakeEnv(render=False)
```
This will disable pygame initialization.

Alternatives:
  [PyGame Learning Environment](http://pygame-learning-environment.readthedocs.io/) is another great reinforcement learning environment. They have their own Snake game!
