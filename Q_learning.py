#!/usr/bin/env python
# coding: utf-8

# Python code to simulate a slotted system with a single queue and binomial IID batch arrivals
# 
# To run the file just run each cell, you can tweak each paramter according to your needs
# 

# In[1]:


import numpy as np


# In[15]:


#defining the paramters
n_episodes = 20000 #no of episodes for training
max_queue_length = 150
n_actions = 2 #no of actions, K or M
time_steps = 1000 #number of time steps in a single episode
N = 40 #batch size
learning_rate = 0.1 #learning rate
gamma = 0.9 #discount for the future rewards
epsilon = 0.2 #paramter for the epsilon greedy policy
P = 0.5 #success probability
M = 50 #packet serving with cost of C
K = 8 #packet serving with cost of 0
C = 30 # reward


# In[16]:


#Initialize Q values
#assuming first value to be K, next value to be M
Q = np.zeros((max_queue_length+1, n_actions))


# In[17]:


#defining our Epsilon-greedy policy for the tradoff between exploration and exploitation, to choose an action
def epsilon_greedy_policy(state, epsilon):
  if np.random.rand() < epsilon:
    return np.random.randint(n_actions)
  else:
    return np.argmax(Q[state])


# In[18]:


#defining the Q-learning algorithm to converge to an optimal policy
for episode in range(n_episodes):
  #setting an initial length of the queue
  state = np.random.randint(0,max_queue_length+1)
  

  for time_step in range(time_steps):
    #taking an action based on the policy
    action = epsilon_greedy_policy(state, epsilon)


    received_packets = np.random.binomial(N, P)

    #0 means K and 1 means M
    if action == 0:
      reward = -state - 0
      new_state = state - min(state,K) + received_packets
    else:
      reward = -state - C
      new_state = state - min(state,M) + received_packets

    new_state = min(max(0, new_state), max_queue_length)

    Q[state,action] += learning_rate*(reward + gamma*np.max(Q[new_state]) - Q[state, action])
    state = new_state


policy = np.argmax(Q, axis=1)
print("Policy:", policy)

print("Q-Table")
print(Q)


# In[23]:


first_values = [i[0] for i in Q]
second_values = [i[1] for i in Q]

import matplotlib.pyplot as plt

plt.grid(True)
plt.title("Q-value plots for Tabular Learning")
x_values = np.arange(0,151,1)
plt.plot(x_values, first_values)
plt.plot(x_values, second_values)
plt.xlabel("Queue lengths")
plt.ylabel("Q-values for each length")
plt.legend(["Q-value for action 0","Q-value for action 1"])
plt.show()


# In[25]:


np.save('Q_table.npy', Q)
Q_table = np.load('Q_table.npy')
print(Q_table)

