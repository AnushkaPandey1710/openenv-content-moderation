import random
from .models import State, Action, StepResult
class ModerationEnvironment:


    def __init__(self, episode_length=20, seed=42):
        self.episode_length = episode_length
        random.seed(seed)
        self.reset()

    def reset(self):
        self.t = 0
        self.current_state = self._generate_post()
        return self.current_state

    def state(self):
        return self.current_state

    def step(self, action: Action):
        self.t += 1

        reward = self._compute_reward(self.current_state, action)

        done = self.t >= self.episode_length

        self.current_state = self._generate_post()

        return StepResult(self.current_state, reward, done)
