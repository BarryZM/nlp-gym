from nlp_gym.data_pools.custom_seq_tagging_pools import UDPosTagggingPool
from nlp_gym.envs.seq_tag_env import SeqTagEnv
from nlp_gym.envs.reward.seq_tagging import EntityF1Score

# data pool
pool = UDPosTagggingPool.prepare("train")
labels = pool.labels()

# reward function
reward_fn = EntityF1Score(dense=True, average="micro")

# seq tagging env
env = SeqTagEnv(possible_labels=labels, reward_function=reward_fn)
for sample, weight in pool:
    env.add_sample(sample, weight)

# play an episode
done = False
state = env.reset()
total_reward = 0
while not done:
    env.render()
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    total_reward += reward
print(f"Episodic reward {total_reward}")