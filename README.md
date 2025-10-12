# ci-github-actions-demo
# CI with GitHub Actions Demo

This repository is a demonstration of Continuous Integration (CI) and other features using GitHub Actions. It was created as a solution for a home assignment.

## Workflows

This project contains two workflows:

### 1. CI Pipeline (`ci.yml`)

This workflow is triggered whenever code is pushed to the `main` branch. It performs the following tasks:
- **Checks out the code:** Uses the `actions/checkout` action.
- **Runs on a Matrix of Python Versions:** It uses a `matrix` build strategy to run the jobs on Python versions 3.7, 3.8, 3.9, and 3.10.
- **Sets up Python:** Configures the environment for each specific Python version from the matrix.
- **Runs Tests:** Executes the Python tests located in `test_main.py` using the `unittest` framework.

### 2. Daily Scheduled Build (`scheduled.yml`)

This workflow is designed to run on a schedule.
- **Trigger:** It uses a `cron` schedule to run automatically every day at midnight (00:00 UTC).
- **Action:** It checks out the code and prints the message "Scheduled build completed successfully!" to the logs.

---
*This project successfully implements basic CI, scheduled jobs, and matrix builds to demonstrate proficiency with GitHub Actions.*
