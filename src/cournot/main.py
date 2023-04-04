import gym
from gym.envs.registration import register
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from multiprocessing import freeze_support
def make_env(num_agents):
    return gym.make("esi_cournotEnv-v0", num_agents=num_agents)

if __name__ == '__main__':
    freeze_support()
    num_envs = 1
    num_agents = 4

    register(
        id='esi_cournotEnv-v0',
        entry_point='src.envs.cournot:CournotEnv',
        max_episode_steps=300,
    )

    env = DummyVecEnv([make_env(num_agents).unwrapped for _ in range(num_envs)])

    model = PPO("MlpPolicy", env, verbose=1,
                learning_rate=1e-3,
                gamma = .99997,
                tensorboard_log="./cournot/"
                )

    # model.load("cournot")
    model.learn(total_timesteps=100)
    model.save("cournot")

    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
        print(f"Rewards: {rewards}")
        print(f"Action: {action}")
