# Week 5 - Token Usage and Budget Estimation

## About this week

In this week, I worked on a small Python program to estimate the token usage and cost of an LLM feature before building it.

The program takes values from environment variables, calculates estimated daily and monthly token usage, estimates the cost, and checks the results against the configured request limits and budget.

## Files in this folder

- `budget.py` - contains the `FeatureBudget` class and the calculations.
- `test_budget.py` - test file (currently empty).
- `requirements.txt` - lists the package needed to run the program.
- `.env` - stores the planning values used by the program. Do not share private values publicly.

## What I learned

- How to estimate input and output tokens for daily requests.
- How to calculate approximate daily and monthly API costs.
- What RPM (requests per minute) and TPM (tokens per minute) mean.
- Why it is useful to keep a safety margin.
- How to compare estimated usage with daily and monthly budgets.

## Configuration

The program reads these values from `.env`:

- `REQUESTS_PER_DAY`
- `AVG_INPUT_TOKENS`
- `AVG_OUTPUT_TOKENS`
- `PEAK_REQUESTS_PER_MINUTE`
- `INPUT_PRICE_PER_MILLION`
- `OUTPUT_PRICE_PER_MILLION`
- `RPM_LIMIT`
- `TPM_LIMIT`
- `MONTHLY_BUDGET_USD`
- `DAILY_BUDGET_USD`
- `SAFETY_MARGIN_PERCENT`

If a value is missing, the program uses the default shown in `budget.py`.

## Setup

1. Open a terminal in this `Week5` folder.
2. Create and activate a Python virtual environment if needed.
3. Install the package:

   ```bash
   pip install -r requirements.txt
   ```

4. Check that the `.env` file has the planning values you want to use.

## Run the program

```bash
python budget.py
```

The program prints estimated token usage, daily and monthly cost, and PASS or REVIEW results for the configured limits and budgets.

## Run tests

The submitted `test_budget.py` file is empty at the moment, so there are no tests in it yet.
