class ModerationResult:
    def __init__(self, text, flagged):
        self.text = text
        self.flagged = flagged


from dataclasses import dataclass

@dataclass
class State:
    toxicity: float          # 0–1
    virality: float          # 0–1
    reports: int             # 0–100
    user_reputation: float   # 0–1

@dataclass
class Action:
    action_type: int  # 0=ALLOW, 1=FLAG, 2=REMOVE, 3=ESCALATE

@dataclass
class StepResult:
    state: State
    reward: float
    done: bool
