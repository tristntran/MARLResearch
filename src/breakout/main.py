"""
"""
from trainer import init_model
from stable_baselines3 import PPO

def main():
    # multiprocess environment
    n_steps = 10000000
    save_every_n = 500000
    
    model = init_model(PPO,'MlpPolicy','CartPole-v1',n_steps)
    count = 0
    while count <= n_steps:
        model.learn(total_timesteps=save_every_n)
        file_name = 'ppo2_cartpole'
        model.save(f"models/{file_name}_steps{count}")
        count += save_every_n

if __name__ == "__main__":
    print("FOO")
    main()