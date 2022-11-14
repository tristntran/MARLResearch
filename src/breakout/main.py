"""
"""
from trainer import train_model
from stable_baselines3 import PPO

def main():
    # multiprocess environment
    n_steps = 100
    model = train_model(PPO,'MlpPolicy','CartPole-v1',n_steps)
    file_name = 'ppo2_cartpole'
    model.save(f"models/{file_name}_steps{n_steps}")

if __name__ == "__main__":
    print("FOO")
    main()