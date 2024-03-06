# -*- coding: utf-8 -*-
"""Q-Value Iteration for Known MDPs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vc_ci13NUqYUsOa9PyaTECkc2OOkPluF
"""

import numpy as np
import matplotlib.pyplot as plt

"""Implementing Q-value iteration"""

#defining the parameters
n_episodes = 30000
max_queue_length = 150
n_actions = 2
N=40
learning_rate = 0.1
gamma = 0.9
epsilon = 0.2
P = 0.5
M = 50
K = 8
C = 30

Q = np.zeros((max_queue_length+1, n_actions))

from scipy.stats import binom
epsilon = 1e-5

for episode in range(n_episodes):
  # prev_Q = Q.copy()

  for state in range(max_queue_length+1):
    for action in range(n_actions):

      if action == 0:
        Q[state, action] = sum([ binom.pmf(k=i,n=N,p=P)*((-state-0)+ gamma*np.max(Q[min((state-min(K,state)+i), max_queue_length)])) for i in range(0,N+1)])
      else:
        Q[state, action] = sum([ binom.pmf(k=i,n=N,p=P)*((-state-C)+ gamma*np.max(Q[min((state-min(M,state)+i), max_queue_length)])) for i in range(0,N+1)])

  # if np.max(np.abs(Q - prev_Q)) < epsilon:
  #    print("No need to continue")
  #    break

policy = np.argmax(Q, axis=1)
print("Policy:", policy)
sum_i = 0
for i in range(len(policy)):
  sum_i = sum_i+policy[i]
  if sum_i == 1:
    print(f"Threshold:{i}")
    break

first_values = [i[0] for i in Q]
second_values = [i[1] for i in Q]

plt.grid(True)
plt.title("Q-value plots for Tabular Learning")
x_values = np.arange(0,151,1)
plt.plot(x_values, first_values)
plt.plot(x_values, second_values)
plt.xlabel("Queue lengths")
plt.ylabel("Q-values for each length")
plt.legend(["Q-value for action 0","Q-value for action 1"])
plt.show()