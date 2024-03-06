# -*- coding: utf-8 -*-
"""Optimal Policy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l-DswPpDhPRrwHy1sWgVWtKzV3LIkiTa
"""

import numpy as np
import matplotlib.pyplot as plt

#defining the paramters
n_episodes = 1000 #no of episodes for training
max_queue_length = 150
n_actions = 2 #no of actions, K or M
time_steps = 10000 #number of time steps in a single episode
N = 40 #batch size
gamma = 0.90 #discount for the future rewards
P = 0.5 #success probability
M = 50 #packet serving with cost of C
K = 8 #packet serving with cost of 0
C = 30 # reward

def policy(state, threshold):
  if state > threshold:
    return 1
  else:
    return 0

mean_rewards = []
for i in range(10,46):
  threshold = i
  reward_list = []

  for episode in range(n_episodes):
    # state = np.random.randint(0, max_queue_length+1)
    state = 0
    total_reward = 0

    for time_step in range(time_steps):

      action = policy(state, threshold)

      received_packets = np.random.binomial(N, P)

      if action == 0:
        reward = state+0
        total_reward += (reward*(gamma**time_step))
        served = min(state, K)
        new_state = state - served + received_packets
      else:
        reward = state+C
        total_reward += (reward*(gamma**time_step))
        served = min(state, M)
        new_state = state - served + received_packets

      new_state = min(max(0, new_state), max_queue_length)

      state = new_state

    reward_list.append(total_reward)

  mean_rewards.append(np.mean(reward_list))

x_values = [i for i in range(10,46)]
plt.xlabel("Thresholds")
plt.ylabel("Long-Run Discounted Cost")
plt.title("Cost vs Threshold")
plt.grid()
plt.plot(x_values,mean_rewards)
plt.scatter(x_values,mean_rewards)
plt.show()
print(10+np.argmin(mean_rewards))