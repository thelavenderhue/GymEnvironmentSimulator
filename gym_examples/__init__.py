from gym.envs.registration import register

register(
    id="gym_examples/IntersectionEnv-v0",
    entry_point="gym_examples.envs:IntersectionEnv",
)
