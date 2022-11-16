import time

import gym
import numpy as np
import os

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

from typing import Callable

if __name__=='__main__':
    env_id = "Breakout-v4"
    num_cpu = 6  # Number of processes to use
    # Create the vectorized environment
    # By default, we use a DummyVecEnv as it is usually faster (cf doc)
    vec_env = make_vec_env(env_id, n_envs=num_cpu)

    model = PPO('MlpPolicy', vec_env, verbose=1)
    os.makedirs("model", exist_ok=True)
    n_steps_arr = [10, 100, 1000,10000, 100000]
    for n_steps in n_steps_arr:
        model.learn(n_steps)
        model.save(f"model/breakout{n_steps}")
