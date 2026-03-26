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

    def _generate_post(self):
    return State(
        toxicity=random.uniform(0, 1),
        virality=random.uniform(0, 1),
        reports=random.randint(0, 100),
        user_reputation=random.uniform(0, 1)
    )

    def _generate_post(self):
    return State(
        toxicity=random.uniform(0, 1),
        virality=random.uniform(0, 1),
        reports=random.randint(0, 100),
        user_reputation=random.uniform(0, 1)
    )


    def _compute_reward(self, state, action):
    toxicity = state.toxicity

    # Ground truth (hidden logic)
    is_harmful = toxicity > 0.6

    if action.action_type == 2:  # REMOVE
        if is_harmful:
            return +1.0
        else:
            return -0.5

    elif action.action_type == 0:  # ALLOW
        if is_harmful:
            return -1.0
        else:
            return +0.5

    elif action.action_type == 1:  # FLAG
        return 0.2 if is_harmful else 0.0

    elif action.action_type == 3:  # ESCALATE
        return 0.1

    return 0.0

   # STEP 5: Add Realism (IMPORTANT FOR JUDGES) Enhance reward slightly:

    virality_penalty = state.virality * 0.5

if is_harmful and action.action_type == 0:
    return -1.0 - virality_penalty

STEP 6: Test Locally (MANDATORY)
env = ModerationEnvironment()

state = env.reset()

for _ in range(5):
    action = Action(action_type=2)
    result = env.step(action)
    print(result)

#STEP 7: Add Utility (VERY HELPFUL)
def state_dict(self):
    return {
        "toxicity": self.current_state.toxicity,
        "virality": self.current_state.virality,
        "reports": self.current_state.reports,
        "user_reputation": self.current_state.user_reputation
    }

#STEP 8: Integration Requirement

env.reset()
env.step(Action(2))
env.state()
