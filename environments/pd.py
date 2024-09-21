import gym
import numpy as np
# from gym.spaces import Discrete, Tuple
from ray.rllib.env import MultiAgentEnv
import wandb

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

    def __init__(self, horizon=1, **kwargs):
        self.horizon = horizon
        print("max_steps",self.horizon)
        # self.payout_mat = np.array([[-1., 0.], [-3., -2.]]) # for PD
        self.payout_mat = np.array([[0., 2.], [-1., 0.]]) # for IPC
        self.dummy_state = np.array([1., 0.]) # alternative dummy observation [1, 0]
        self.step_count = 0

        self.num_outputs = 2
        self.action_space = gym.spaces.Discrete(2)
        # self.observation_space = gym.spaces.Discrete(1)
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(2,))  # alternative dummy observation [1, 0]
        self.metrics = {'transfers':0} # initial transfer is 0

    def reset(self):
        self.step_count = 0
        return {
            "a0": self.dummy_state,
            "a1": self.dummy_state
        }
        # return {
        #     "a0": 0,
        #     "a1": 0
        # }

    def step(self, actions):
        ac0 = actions["a0"]
        ac1 = actions["a1"]
        self.step_count += 1
        wandb.log({'horizon':self.horizon})
        # Compute rewards for both agents
        rewards = {
            "a0": self.payout_mat[ac1][ac0],
            "a1": self.payout_mat[ac0][ac1]
        }

        social_welfare = rewards["a0"] + rewards["a1"]

        # Determine if the episode is done
        done = self.step_count == self.horizon
        dones = {"__all__": done}

        # infos = {"a0": {}, "a1": {}}

        # Log actions, rewards, and social welfare in the infos dictionary
        infos = {
            "a0": {
                "action of a0": ac0,
                "reward of a0": rewards["a0"],
                "social_welfare": social_welfare
            },
            "a1": {
                "action of a1": ac1,
                "reward of a1": rewards["a1"],
            }
        }


        # Return the next observations, rewards, done flags, and infos
        return {
            "a0": self.dummy_state,
            "a1": self.dummy_state
        }, rewards, dones, infos