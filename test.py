from snake import SnakeEnv

env = SnakeEnv()
# env.interactive()
for episode in range(10):
    observation = env.reset()
    while True:
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
