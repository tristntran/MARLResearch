from gym import Env, spaces
import numpy as np

MAX_PERIODS = 100
START_HEALTH = 30
ACTION_PENALTY = 100
class HealthCareEnv(Env):

    def __init__(self):
        """.ci.yml"""
        super(HealthCareEnv, self).__init__()
        # Define the action space
        self.action_space = spaces.Box(low=0, high=100, shape=(2,), dtype=np.uint8)
        # Define the observation Space
        self.observation_space = spaces.Box(low=0, high=100, shape=(3,), dtype=np.uint8)

    def reset(self):
        """
        sets up the problem from scratch
        """
        self.period = 0
        self.fitness = START_HEALTH
        self.joy = 0
        self.savings = 0
        self.shocks = 0
        return self._next_observation()

    def step(self, action):
        """
        applies an action onto the space

        :param action: _description_
        :return: _description_
        """
        self.savings += 100
        self._take_action(action)
        self.period += 1
        delay_modifier = self.period/MAX_PERIODS
        reward = self.joy * delay_modifier if self.valid_action(action) else - ACTION_PENALTY
        done = self.shocks >= 6 or self.fitness <= 0
        obs = self._next_observation()
        return obs, reward, done, {}

    def valid_action(self, action):
        """
        assesses whether or not a valid action is made

        :param action: _description_
        """
        return sum(action) <= 100

    def _get_shocked(self):
        """.ci.yml"""
        pshock = (np.exp(0.02 * self.period)+ np.exp(0.05 * self.shocks - 1.95))*(1-1.2*(self.fitness/(self.fitness + 40)))
        return np.random.random() <= pshock

    def _next_observation(self):
        """
        gets the next observation for the plan
        """
        obs = np.array([self.period, self.savings, self.fitness])
        return obs

    def _take_action(self, action):
        """
        takes the current action and then returns the joy

        :param action: _description_
        """
        self.fitness = 2/3 * self.fitness + 0.3 * action[0] * self.savings
        self.joy +=  (1 - self.shocks/6)*  action[1] / (action[1]+20)
        self.shocks += self._get_shocked()
    
    def render(self, reset_params=False):
        print(f"Fitness {self.fitness}\nJoy {self.joy}\nPeriod{self.period}")