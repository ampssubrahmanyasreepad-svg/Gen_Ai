# Week 4 - Comparing Tokenizers

## About this week

In this week, I worked with tokenizers using the Hugging Face Transformers library. A tokenizer splits text into smaller parts called tokens and converts those tokens into token IDs that a model can process.

The program compares three tokenizer types using sample sentences in English, Telugu, and Hindi.

## Files in this folder

- `tokenizer_comparison.py` - loads the tokenizers, processes the sample sentences, and prints the tokens, token IDs, and token count.
- `requirements.txt` - contains the Python packages needed for this task.

## Tokenizers used

- BPE - GPT-2 (`gpt2`)
- WordPiece - Multilingual BERT (`bert-base-multilingual-cased`)
- SentencePiece - XLM-R (`xlm-roberta-base`)

## What I learned

- What tokenization means.
- How text is split into tokens.
- How token IDs are created.
- That different tokenizers can split the same sentence differently.
- How tokenizer output can be compared across English, Telugu, and Hindi.

## Setup

1. Open a terminal in this `Week4` folder.
2. Create and activate a Python virtual environment if needed.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Keep an internet connection available the first time you run the program because the tokenizer files may need to be downloaded.

## Run the program

```bash
python tokenizer_comparison.py
```

The terminal displays the input text, tokens, token IDs, and token count for each tokenizer.

## Note

The model/tokenizer files are downloaded by the Transformers library when they are not already available on the computer.
