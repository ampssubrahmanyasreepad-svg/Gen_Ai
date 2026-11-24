# Week 3 - Tracking LLM Usage

## About this week

In this week, I extended the LLM client from the previous week. The program is designed to collect information about each model request, such as the number of input and output tokens, response time, estimated cost, and whether the request was successful.

I also added a usage logger that saves the details in MongoDB. The client includes retry handling for some temporary errors.

## Files in this folder

- `main.py` - starts the program and lets me select Gemini or Ollama.
- `llm_client.py` - contains the provider and client logic, token information, response time, estimated cost, and retry handling.
- `usage_logger.py` - saves usage records in MongoDB.
- `test_client.py` - tests the client with a fake provider and fake logger.
- `.env` - stores configuration values such as API and database connection details. Do not share this file publicly.
- `requirements.txt` - lists the Python packages used by this week.

## What I learned

- How token usage can be measured.
- How to calculate an estimated API cost from token counts.
- How to measure response time.
- Why temporary API errors may need retries.
- How to save usage details in a MongoDB collection.
- How to test the client without making a real API call.

## Setup

1. Open a terminal in this `week3` folder.
2. Create and activate a Python virtual environment if needed.
3. Install the packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Add the required values to a local `.env` file. The code reads `GEMINI_API_KEY` and `MONGODB_URI`. The cost settings `GEMINI_INPUT_PRICE_PER_MILLION` and `GEMINI_OUTPUT_PRICE_PER_MILLION` are optional and default to `0`.
5. Make sure the MongoDB connection string points to a database you are allowed to use.

## Run the program

```bash
python main.py
```

Choose a provider and enter a prompt when asked.

## Run the test

```bash
python -m unittest test_client.py
```

## Important code note

While checking the submitted `llm_client.py`, I noticed that the `GeminiProvider.__init__` method appears to be outside the class because of its indentation. This may cause the Gemini option to fail. It should be checked and corrected before expecting the program to run. I have not changed the Python code in this folder.

## Database note

The logger uses the database named `llm_monitoring` and the collection named `api_usage`.
