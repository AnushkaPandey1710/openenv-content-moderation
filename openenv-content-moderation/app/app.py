from env.environment import ModerationEnvironment

def main():
    env = ModerationEnvironment()
    result = env.step("Test input")
    print(result)

if __name__ == "__main__":
    main()


########################################
STEP 1: Setup FastAPI App
from fastapi import FastAPI
from env.environment import ModerationEnv
from env.models import Action

app = FastAPI()

env = ModerationEnv()

STEP 2: Health Check (VERY IMPORTANT)
@app.get("/")
def health():
    return {"status": "ok"}

👉 Used to verify deployment quickly

🔁 STEP 3: Implement /reset
@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state.__dict__}
▶️ STEP 4: Implement /step
@app.post("/step")
def step(action: dict):
    act = Action(action_type=action["action"])
    result = env.step(act)

    return {
        "state": result.state.__dict__,
        "reward": result.reward,
        "done": result.done
    }
📊 STEP 5: Implement /state
@app.get("/state")
def get_state():
    state = env.state()
    return {"state": state.__dict__}
📋 STEP 6: Implement /tasks
@app.get("/tasks")
def tasks():
    return {
        "tasks": ["easy", "medium", "hard"],
        "action_schema": {
            "type": "int",
            "range": [0, 3]
        }
    }
🧪 STEP 7: Add /baseline (connect later with Lead)
from evaluation.evaluate import run_baseline

@app.get("/baseline")
def baseline():
    scores = run_baseline()
    return scores
🧪 STEP 8: Add /grader
from evaluation.grader import grade_episode

@app.get("/grader")
def grader():
    score = grade_episode()
    return {"score": score}
📦 STEP 9: requirements.txt
fastapi
uvicorn
numpy
🐳 STEP 10: Dockerfile (VERY IMPORTANT)
FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "7860"]
🧪 STEP 11: Run Locally (MANDATORY)
uvicorn app.app:app --reload
Test endpoints:
curl -X GET localhost:8000/
curl -X POST localhost:8000/reset
curl -X POST localhost:8000/step -H "Content-Type: application/json" -d '{"action":2}'
curl -X GET localhost:8000/tasks

👉 ALL must work

🔗 STEP 12: Hugging Face Deployment
Steps:
Go to Hugging Face → Create Space
Choose:
SDK: Docker
Push repo:
git push
🧪 STEP 13: Verify Deployment

Test:

https://your-space-url/reset

👉 Must return JSON

Common Mistakes (VERY IMPORTANT)

❌ Wrong port (must be 7860)
❌ Wrong path (app.app:app)
❌ Returning non-JSON
❌ Not handling POST properly
❌ Missing endpoints


