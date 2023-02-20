from gym.envs.registration import register
register(
    id='esi_healthcareEnv-v0',
    entry_point='src.healthcare:HealthCareEnv',
    max_episode_steps=300,
)
