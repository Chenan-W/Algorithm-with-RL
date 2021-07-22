import gym
env = gym.make('CartPole-v0') #1.构造env， 根据name指定 
env.reset()                                           #2.初始化env
for _ in range(1000):
    env.render()                                   #3.渲染
    env.step(env.action_space.sample()) # take a random action#4.action
env.close()
