import gym
from gym import Env, spaces
import numpy as numpy

START_HEALTH = 30
class HealthCareEnv(Env):

    def __init__(self):
        """.ci.yml"""
        # fix this
        self.action_space = tuple(spaces.Discrete(100), spaces.Discrete(100))
        # fix this
        self.observation_space = spaces.Box(low=0, high=255, shape=
                    (HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

    def reset(self):
        """
        sets up the problem from scratch
        """
        self.period = 0
        self.fitness = START_HEALTH
        self.savings = 0
        self.shocks = 0

    def step(self, action):
        """
        applies an action onto the space

        :param action: _description_
        :return: _description_
        """
        self.savings += 1
        reward += self._take_action(action)
        self.shocks += self._get_shocked()
        self.period += 1
        self.current_step += 1
        
        done = False
        obs = self._next_obeservation()
        return obs, reward, done, {}

    def _get_shocked(self):
        """.ci.yml"""
        pshock = (np.exp(0.02 * self.period)+ np.exp(0.05 * self.shocks - 1.95))(1-1.2*(self.fitness/(self.fitness + 40)))
        return np.random.random() <= pshock

    def _next_obeservation():
        """
        gets the next observation for the plan
        """
        obs = 0
        return obs

    def _take_action(self, action):
        """
        takes the current action and then applies shock

        :param action: _description_
        """
        self.fitness = 2/3 * self.fitness + 0.3 * action[0] * self.savings
        result = (1 - self.shocks/6)*  action[1] / (action[1]+20)
        return result