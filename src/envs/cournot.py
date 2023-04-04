"""
Code for a cournot equilibrium optimization.

The logic goes as follows.
Each firm decides its quantity produced q_i.

A firm's profit is equal to the inverse demand

Profit(q) = p(q)*q_i
"""
import numpy as np
import gym
from gym import spaces

def inverse_demand(quantity_vec: np.ndarray)->float:
    """
    gets the inverse demand function based off of the quantity vector which is a
    vector of integers

    :param quantity_vec: vector of integers
    :return: floating point number representing the price in an oligopoly market
    """
    price = 0
    return price

def calc_profit(price, quantity, cost) -> float:
    """
    Calculate the profit given a specific price, quantity and cost or a single firm

    :param price: price in the market
    :param quantity: quantity produced by a single firm
    :param cost: cost used by a firm
    :return: value for profit.
    """
    return (price - cost) * quantity

def calc_profit_vec(quantity_vec:np.array, cost_vec: np.array) -> np.ndarray:
    """
    calculates a vector of values representing profits for all vectors

    :param quantity_vec: vector of quantities produced by each firm i
    :param cost_vec: vector of costs defined for each firm i
    :return: vector of profits achieved by each firm i
    """
    price = inverse_demand(quantity_vec)
    profit_vec = np.zeros(quantity_vec.shape)
    for i, quant in enumerate(quantity_vec):
        profit_vec[i] = calc_profit(price, quant, cost_vec[i])
    # profit_vec = price*quantity_vec - cost_vec * quantity_vec
    return profit_vec


NUM_FIRMS = 4
INITIAL_CASH = np.array([[100,20,20,20]])
FIRM_COSTS = np.ones(NUM_FIRMS) * 5
MAX_PERIODS = 20
class CournotEnv(gym.Env):
    """
    Class environment that models a repeated equilibrium game.

    inherits from the gym.Env class
    """
    def __init__(self, num_envs = 1, num_agents = NUM_FIRMS):
        """
        define the observation space and action space variables
        The observation space is defined as an obsservation space representing
        the amount of cash that each firm has on hand

        The action space represents possible actions they can take.
        """
        super(CournotEnv, self).__init__()
        self.num_envs = num_envs
        self.num_agents= num_agents
        # Define observation space and action space for each agent
        self.observation_space = spaces.Box(low=0, high=999, shape=(self.num_agents,), dtype=np.int32)
        self.action_space = spaces.Box(low=0, high=999, shape=(self.num_agents,), dtype=np.int32)

    def reset(self):
        global INITIAL_CASH
        # Initialize environment and return initial observations
        self.cash = INITIAL_CASH
        self.period = 0
        return self._next_observation()

    def step(self, actions):
        cash_mask = self.cash > 0
        actions = cash_mask * actions
        rewards = self._take_action(actions)
        obs = self._next_observation()
        self.period += 1
        done = self.period >= MAX_PERIODS
        return obs, rewards, done, {}

    def _take_action(self, actions):
        # Take actions for each agent and return next observations, rewards, and done flag
        rewards = np.zeros((self.num_envs, self.num_agents))
        for i in range(self.num_envs):
            rewards[i] = calc_profit_vec(actions[i], FIRM_COSTS)
        self.cash = self.cash + rewards
        return rewards

    def _next_observation(self):
        return np.array(self.cash, dtype=np.int32)

    def render(self, mode='human'):
        # Render the current state of the environment, if desired
        pass