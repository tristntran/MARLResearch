import gym
from gym import spaces
import numpy as np

NUM_AGENTS = 4

class MultiAgentEnv(gym.Env):
    def __init__(self):
        # Define observation space and action space for each agent
        self.observation_space = [spaces.Box(low=-10, high=10, shape=(2,), dtype=np.float32) for _ in range(NUM_AGENTS)]
        self.action_space = [spaces.Discrete(2) for _ in range(NUM_AGENTS)]

    def reset(self):
        # Initialize environment and return initial observations
        obs = [np.random.uniform(low=-10, high=10, size=(2,)) for _ in range(NUM_AGENTS)]
        self.period = 0
        return obs

    def step(self, actions):
        # Take actions for each agent and return next observations, rewards, and done flag
        obs = []
        rewards = []
        # Firm observes sell-off value

        # firm makes decision to exit and invest
        
        # entrant obeserves entry cost and makes entry decisions
        # incumbent firsm compete in market and receive profit
        # exiting firms receive sell-off values
        # investment shock outcomes are determined
        # new entrants enter
        # industry takes on new state
        for i in range(NUM_AGENTS):
            obs_i = self.observation_space[i].sample()
            obs.append(obs_i)
            reward_i = self.get_profit(i, actions)
            rewards.append(reward_i)
        done = False
        return obs, rewards, done, {}

    def get_profit(self, agent_idx: int, actions):
        return actions[agent_idx]/np.sum(actions)

    def _next_observation(self):
        ...

    def render(self, mode='human'):
        # Render the current state of the environment, if desired
        pass
