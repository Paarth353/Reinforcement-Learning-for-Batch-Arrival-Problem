# Reinforcement-Learning-for-Batch-Arrival-Problem

Problem statement![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/f2d61160-445e-4aee-be5f-08fe1679e8d7)

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

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/81b639e3-b04a-48a6-84f8-67392914dee4)


![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/cc58554a-a0d8-4bcd-96a6-734fe184a5c0)

Tabular Q-learning vs. Q-iteration (model based)![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/60dbbf45-146c-48f1-af3b-ca03b94c77df)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/a920c78b-344b-4e28-9e78-51f3e919d2d5)

![image](https://github.com/Paarth353/Reinforcement-Learning-for-Batch-Arrival-Problem/assets/99269831/05bce4b9-cb53-4819-a0c4-1d2e3d3d3a00)






