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
model = PPO("MlpPolicy", env, verbose=1,
            learning_rate=1e-3,
            gamma = .9,
            tensorboard_log="./healthcare/"
            )
# model.load("healthcare")
model.learn(total_timesteps=1000000)
model.save("healthcare")
obs = env.reset()
done = False
while not done:
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
    print(f"Rewards: {rewards}")
    print(f"Action: {action}")