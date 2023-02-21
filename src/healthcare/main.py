import gym
from gym.envs.registration import register
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
register(
    id='esi_healthcareEnv-v0',
    entry_point='src.envs.healthcare:HealthCareEnv',
    max_episode_steps=300,
)
env = gym.make("esi_healthcareEnv-v0")
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=25000)
model.save("healthcare")
obs = env.reset()
for i in range(100):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()