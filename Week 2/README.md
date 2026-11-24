# Week 2 - Working with Different LLM Providers

## About this week

In this week, I worked on connecting my Python program with different Large Language Model (LLM) providers. I added two options: Gemini, which runs using an online API, and Ollama, which can run a model locally on my laptop.

I also used a common client so that the main program does not need to handle each provider separately.

## Files in this folder

- `main.py` - asks me to choose Gemini or Ollama, takes a question, and prints the answer.
- `llm_client.py` - contains the provider classes and the common LLM client.
- `test_client.py` - contains a simple unit test using a fake provider.
- `.env` - stores the Gemini API key. This file should not be shared publicly.
- `requirements.txt` - package list (currently empty).

## What I learned

- What an LLM provider is.
- How to connect to Gemini using an API key.
- How to send a prompt to Ollama running locally.
- Why a common interface is useful when working with more than one provider.
- How to write a basic unit test with Python's `unittest`.

## Setup

1. Open a terminal in this `week2` folder.
2. Create and activate a Python virtual environment if you want to keep the packages separate.
3. Install the packages used by the code:

   ```bash
   pip install google-genai requests python-dotenv
   ```

4. For Gemini, add your API key to a `.env` file:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

5. For Ollama, install and start Ollama separately, and make sure the `llama3.2` model is available.

## Run the program

```bash
python main.py
```

Choose `gemini` or `ollama`, then enter a question.

## Run the test

```bash
python -m unittest test_client.py
```

## Note

The `requirements.txt` file is empty in the submitted folder, so I have included the install command above based on the packages imported by the Python files.
