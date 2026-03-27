# OpenEnv Content Moderation

A modular framework to **simulate, evaluate, and benchmark AI content moderation systems** using OpenEnv.

## Features

- Plug-and-play moderation environment
- Evaluation pipeline with scoring system
- Baseline moderation model
- Docker-ready setup
- CI/CD with automated evaluation

---

## Project Structure

**1. Problem**

Content moderation at scale is difficult due to ambiguity and trade-offs

**2. Environment**
state variables
action space

**3. Reward Logic**

Explain:

punish missed harmful content
penalize over-censorship

**4. Tasks**

Explain:

easy / medium / hard
**5. How to Run**
pip install -r requirements.txt
python evaluation/evaluate.py

**6. API Endpoints**

List:

/reset
/step
/baseline
/grader
