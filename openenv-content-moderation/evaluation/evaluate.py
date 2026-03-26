from evaluation.tasks import TASKS
from evaluation.baseline import baseline_model
from evaluation.grader import grade

def run_evaluation():
    score = 0
    for task in TASKS:
        pred = baseline_model(task["input"])
        score += grade(pred, task["expected"])
    print(f"Score: {score}/{len(TASKS)}")

if __name__ == "__main__":
    run_evaluation()
