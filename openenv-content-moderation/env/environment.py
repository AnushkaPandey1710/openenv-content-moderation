class ModerationEnvironment:
    def __init__(self, config=None):
        self.config = config or {}

    def reset(self):
        return "Environment reset"

    def step(self, input_text):
        return {"input": input_text, "flagged": False}
