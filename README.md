# Reinforcement-Learning-for-Batch-Arrival-Problem

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/f2d61160-445e-4aee-be5f-08fe1679e8d7)

- Slotted System, Single Queue with Binomial i.i.d batch arrivals
- We have a choice to serve K packets at a cost of 0 or M packets with a cost of C 
- Reward = Queue Length at the beginning of episode + Cost of serving
- The queue is capped at a Max queue length 
- The task is to find the optimal policy such that the long run expected discounted reward is maximum


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/3bbb72a4-c069-4987-959c-60d883acc375)


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/2fa7e681-3bb8-481f-a57e-8d7b839f1860)


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/5a95dc7d-4770-4a55-9e1a-66deabf2b9ea)

- State: Current queue length
- Action: number of packets to be served
- Can be K or M
- Update rule for tabular “model free” Q-learning

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/e32f0fa4-4255-448d-8d78-8ad09ed7da32)

- 𝑅_(𝑡+1) is the reward when moving from the state 𝑆_𝑡  to the state 𝑆_(𝑡+1) and α is the learning rate
-〖𝛾⋅max┬𝑎〗⁡〖𝑄(𝑆_(𝑡+1), 𝑎)〗   is the discounted future rewards
- 𝑄(𝑆_𝑡  , 𝐴_𝑡) is the current Q-value for state 𝑆_𝑡 and action 𝐴_𝑡

Tabular Q-learning vs. Policy exploration![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/04507934-a259-4939-a705-8abc442f1ccb)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/dea10b4b-3a4d-41e2-a12a-ad696bd12e10)


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/cc58554a-a0d8-4bcd-96a6-734fe184a5c0)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/60dbbf45-146c-48f1-af3b-ca03b94c77df)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/a920c78b-344b-4e28-9e78-51f3e919d2d5)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/05bce4b9-cb53-4819-a0c4-1d2e3d3d3a00)


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/cdb9341b-f59b-4773-a598-7f505d1296b1)

- We can compute the exact transition probabilities <br/><br/>
![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/68c39a07-4ade-435d-9b5a-6576f0bb6341)
- We also know the exact rewards <br/><br/>
![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/acf905d3-91bb-49f8-8f8e-ce3ddc529f70)
- We can easily iterate through several steps and in each step, update the Q value of each state-action pair until the Q-values converge to optimal values
![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/50ab25af-c824-434f-b99a-717febd9f2de)


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/00318ea0-c9c6-4a7d-8bd2-d2530bb533c5)


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/a1c90ae2-8cff-428e-9ecd-74a7ae46c20b)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/6606b554-941a-459d-b64d-6b8c3a55ce38)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/d9ef4c99-aad4-42bb-a897-fc7d32484d54)

- For a certain number of steps, we collect some samples by taking actions according to current policy and add it to a replay buffer which stores the “past experiences”

- We sample a minibatch from the replay buffer and train our model using these samples. This is done to eliminate the high correlation issue when we use sequential states, and this prevents overfitting.

- We use two models, the main Q-network and a target network.
- Q-network is updated regularly
- Target network is the older version, updated occasionally with the exact copy of weights of the Q-network
- This helps in keeping the target values constant for some time and adds stability to the model
- We use stochastic gradient decent on the weights using the constant target values for the loss function

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/4fc79127-aa85-43f6-b9e4-803ef28a97f1)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/e823c590-046e-4bde-ac5d-2723e8a21259)


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/968c5569-9f9d-40a1-bd08-da244d25a7b0)
