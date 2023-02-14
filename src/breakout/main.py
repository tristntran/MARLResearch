import time

import gym
import numpy as np
import os
from collections import OrderedDict
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.atari_wrappers import AtariWrapper

from typing import Callable

if __name__=='__main__':
    env_id = "Breakout-v4"
    num_cpu = 6  # Number of processes to use
    # Create the vectorized environment
    # By default, we use a DummyVecEnv as it is usually faster (cf doc)
    
    hyperparams = OrderedDict([('batch_size', 256),
             ('clip_range', 'lin_0.1'),
             ('ent_coef', 0.01),
             ('env_wrapper',
              ['stable_baselines3.common.atari_wrappers.AtariWrapper']),
             ('frame_stack', 4),
             ('learning_rate', 'lin_2.5e-4'),
             ('n_envs', 8),
             ('n_epochs', 4),
             ('n_steps', 128),
             ('n_timesteps', 10000000.0),
             ('policy', 'CnnPolicy'),
             ('vf_coef', 0.5),
             ('normalize', False)])
    vec_env = make_vec_env(env_id, n_envs=num_cpu)
    model = PPO('MlpPolicy', vec_env, ent_coef = hyperparams["ent_coef"],
                n_epochs = 4, verbose=1)
    os.makedirs("model", exist_ok=True)

    model.learn(10000000)
    model.save(f"model/breakout{'new'}")
