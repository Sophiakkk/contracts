import gym
import numpy as np
# from gym.spaces import Discrete, Tuple
from ray.rllib.env import MultiAgentEnv

# class IteratedPrisonersDilemma(gym.Env):
class PD(MultiAgentEnv):
    """
    A two-agent vectorized environment for the Prisoner's Dilemma game.
    Possible actions for each agent are (C)ooperate and (D)efect.
    """
    NAME = 'IPD'
    NUM_AGENTS = 2
    NUM_ACTIONS = 2
    NUM_STATES = 1 

    def __init__(self, max_steps=1, **kwargs):
        self.max_steps = max_steps
        self.payout_mat = np.array([[-1., 0.], [-3., -2.]])
        self.dummy_state = np.array([1., 0.])
        self.step_count = None

        self.num_outputs = 2
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Discrete(1)
        # self.observation_space = gym.spaces.Box(low=np.array([0.0, 0.0, 0.0, 0.0]), high=np.array([1.0, 1.0, 2.0, 0.0]), dtype=np.float32)
        print("Running IPD")

        self.metrics = {'transfers':0} # initial transfer is 0

    def reset(self):
        self.step_count = 0
        # return observations for each agent
        return {
            "a0": self.dummy_state,
            "a1": self.dummy_state
        }

    # def compute_equality(self,reward_dict): 
    #     eq = 0 
    #     total_sum = 0
    #     reward_dict = {k:sum(v) for k,v in reward_dict.items()}
    #     n = len(reward_dict.keys())
    #     for i in reward_dict.keys(): 
    #         for j in reward_dict.keys(): 
    #                 eq += abs(reward_dict[i] - reward_dict[j])
    #         total_sum += reward_dict[i]
    #     if total_sum ==0 :
    #         total_sum = 0.001
    #     eq = 1 - eq/(2*n*total_sum)
    #     return eq

    # def compute_sustainability(self,reward_dict): 
    #     avg_times =[] 
    #     for k in reward_dict.keys():
    #         t_sum = 0 
    #         for t,i in enumerate(reward_dict[k]):
    #             t_sum += t*i
    #         denom = sum(reward_dict[k]) 
    #         denom = max(denom,1)
    #         avg_times.append(t_sum/denom)
    #     return np.mean(avg_times)

    def step(self, actions):
        # ac0, ac1 = actions
        # self.step_count += 1

        # rewards = np.array([self.payout_mat[ac1][ac0], self.payout_mat[ac0][ac1]])
        # # print("rewards:",rewards)

        # done = (self.step_count == self.max_steps)

        # return self.dummy_state, rewards, done

        # print(actions)

        ac0 = actions["a0"]
        ac1 = actions["a1"]
        self.step_count += 1

        # Compute rewards for both agents
        rewards = {
            "a0": self.payout_mat[ac1][ac0],
            "a1": self.payout_mat[ac0][ac1]
        }

        # Determine if the episode is done
        done = self.step_count == self.max_steps
        dones = {"__all__": done}

        # Info can be an empty dictionary for now
        infos = {"a0": {}, "a1": {}}

        # Return the next observations, rewards, done flags, and infos
        return {
            "a0": self.dummy_state,
            "a1": self.dummy_state
        }, rewards, dones, infos

