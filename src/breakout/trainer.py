"""
_summary_


"""

def train_model(ALGO: callable, policy: str, env: str, n_steps: int, ):
    model = ALGO(policy, env, verbose=1)
    model.learn(total_timesteps=n_steps)
    return model

def increase_training(model, n_steps):
    model.learn(total_timesteps=n_steps)
    model.save("models/ppo2_cartpole")