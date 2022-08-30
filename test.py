import gym_examples
import gym

env = gym.make('gym_examples/GridWorld-v0', render_mode='human')

import time 

# Number of steps you run the agent for 
num_steps = 1500

obs = env.reset()

for step in range(num_steps):
    # take random action, but you can also do something more intelligent
    # action = my_intelligent_agent_fn(obs) 
    action = env.action_space.sample()
    
    # apply the action
    obs, reward, done, info = env.step(action)
    
    # Render the env
    # env.render()

    # Wait a bit before the next frame unless you want to see a crazy fast video
    time.sleep(0.001)