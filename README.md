# Chatbot With Memory (Beginner GenAI Project)

A very small GenAI project that shows **one idea**: the difference between a
chatbot that forgets everything and a chatbot that remembers the conversation.

No LangChain, no vector database, no frameworks. Just plain Python, a few API
calls, a Python list, and Streamlit.

---

## 🚀 Live Demo

**Try the deployed chatbot:**  
[Open Chatbot With Memory](https://beginner-app-memory-chatbot-ybqyobwz7rs2npvgjlb9fh.streamlit.app/)

> Replace `https://beginner-app-memory-chatbot-ybqyobwz7rs2npvgjlb9fh.streamlit.app/` with your actual Streamlit app link.

---

## 1. Project objective

Build the same chatbot twice:

- once **without memory**, where every question is sent to the LLM on its own, and
- once **with memory**, where the whole conversation is sent with every question,

so you can see with your own eyes why the second one can remember your name
and the first one cannot.

## 2. What does "conversation memory" mean?

An LLM has no built-in memory. Every API request is completely independent:
the model only sees the text you send in that one request. It does not
remember the previous request at all.

So "giving a chatbot memory" simply means:

> keep the previous messages in a list, and send that list again with the next question.

That is all `memory.py` does. It is a Python list of dictionaries like this:

```python
[
    {"role": "user", "content": "My name is Rahul."},
    {"role": "assistant", "content": "Nice to meet you, Rahul!"},
]
```

**Important distinction:** storing messages on your computer is not the same
as the LLM receiving them. The model only knows what you actually put into the
request. In this project you can see exactly what is sent by looking at the
message-building logic in the chatbot files.

## 3. No memory vs. with memory

| | `no_memory_chatbot.py` | `chatbot.py` / `app.py` |
|---|---|---|
| What is sent to the LLM | system instruction + the current question only | system instruction + all previous messages + the current question |
| Can it remember your name? | No | Yes |
| Where is the history kept? | Nowhere | In a Python list (`memory.py`) or in `st.session_state` |
| Cost of a long chat | Stays the same | Grows, because more text is sent each time |

## 4. Project structure

```
Beginner-streamlit-memory-chatbot/
├── no_memory_chatbot.py # Chatbot WITHOUT memory
├── chatbot.py           # Chatbot WITH memory
├── llm_client.py        # Talks to the LLM and returns text
├── memory.py            # Conversation list and memory functions
├── config.py            # Reads settings and API keys
├── app.py               # Streamlit web UI for the chatbot with memory
├── providers.py         # Provider-related chatbot logic
├── requirements.txt     # Python packages needed
├── README.md            # This file
└── .gitignore           # Files excluded from Git
```

## 5. Prerequisites

- Python 3.10 or newer (`python --version`)
- A terminal (Windows PowerShell is used in the examples below)
- **One** of the following:
  - an OpenAI API key, or
  - a Google Gemini API key, or
  - **Ollama** installed locally (free, no key needed)

## 6. Create and activate a virtual environment

A virtual environment keeps this project's packages separate from the rest of
your computer.

**Windows PowerShell**

```powershell
cd Beginner-streamlit-memory-chatbot
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run this once and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

**macOS / Linux**

```bash
cd Beginner-streamlit-memory-chatbot
python3 -m venv .venv
source .venv/bin/activate
```

## 7. Install the dependencies

```powershell
pip install -r requirements.txt
```

## 8. Configure your `.env` file

Create a `.env` file in your project folder and fill in the values for the
provider you want to use.

For example:

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your-real-key
GEMINI_MODEL=your-model-name
```

Your project can also use OpenAI or Ollama if they are configured in your
code.

| Variable | Meaning | Default |
|---|---|---|
| `LLM_PROVIDER` | `openai`, `gemini` or `ollama` | `gemini` |
| `OPENAI_API_KEY` | Your OpenAI key | *(none)* |
| `OPENAI_MODEL` | OpenAI model name | *(none)* |
| `GEMINI_API_KEY` | Your Google Gemini key | *(none)* |
| `GEMINI_MODEL` | Gemini model name | *(none)* |
| `OLLAMA_BASE_URL` | Where Ollama is running | `http://localhost:11434` |
| `OLLAMA_MODEL` | Ollama model name | *(none)* |
| `SYSTEM_PROMPT` | Instruction given to the assistant | a friendly-assistant message |

Switching providers means changing the provider setting and the required API
configuration. None of the chatbot UI files need to be edited just to change
the provider.

> **Keep your keys private.** Your `.env` file contains real credentials, so it
> must never be committed to Git or shared. The `.gitignore` file in this
> project is used to keep `.env` and other local files out of GitHub.

## 9. Using OpenAI

```
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-real-key
OPENAI_MODEL=your-openai-model
```

Get a key at <https://platform.openai.com/api-keys>. OpenAI API requests may
require billing depending on your account and usage.

## 10. Using Google Gemini

```
LLM_PROVIDER=gemini
GEMINI_API_KEY=your-real-key
GEMINI_MODEL=your-gemini-model
```

Get a key at <https://aistudio.google.com/app/apikey>.

For the deployed Streamlit app, the Gemini API key is stored securely in
**Streamlit Secrets** instead of uploading `.env` to GitHub.

## 11. Using Ollama (free, runs on your computer)

1. Download and install Ollama from <https://ollama.com/download>.
2. Download a model:

   ```powershell
   ollama pull llama3.2
   ```

3. Make sure the Ollama server is running. The desktop app starts it
   automatically; otherwise run:

   ```powershell
   ollama serve
   ```

4. Set this in `.env`:

   ```
   LLM_PROVIDER=ollama
   OLLAMA_BASE_URL=http://localhost:11434
   OLLAMA_MODEL=llama3.2
   ```

No API key is needed and nothing is charged, because the model runs locally.

## 12. Running the applications

```powershell
# Chatbot WITHOUT memory (terminal)
python no_memory_chatbot.py

# Chatbot WITH memory (terminal)
python chatbot.py

# Chatbot WITH memory (web page in your browser)
streamlit run app.py
```

Type `exit` or `quit` to leave the terminal chatbots.

## 13. The demonstration

Ask the **same two questions** to both programs.

**`python no_memory_chatbot.py`**

```
You: My name is Rahul, and I work as a Python developer.
Assistant: Nice to meet you, Rahul!

You: What is my name and profession?
Assistant: I don't have that information. Could you tell me your name
           and what you do?
```

**`python chatbot.py`**

```
You: My name is Rahul, and I work as a Python developer.
Assistant: Nice to meet you, Rahul!

You: What is my name and profession?
Assistant: You are Rahul, and you work as a Python developer.
```

Same model, same key, same question. The only difference is that `chatbot.py`
also sent the earlier two messages in the second request.

## 14. Common errors and how to fix them

| Message | What it means | Fix |
|---|---|---|
| `Configuration problem: OPENAI_API_KEY is missing.` | No key was found in `.env` | Check your `.env` and provider configuration |
| `LLM_PROVIDER is 'Openai'. Please use one of: ...` | Typo in the provider name | Use lowercase `openai`, `gemini` or `ollama` |
| `Could not reach Ollama at http://localhost:11434` | Ollama is not running | Start the Ollama app, or run `ollama serve` |
| `Ollama request failed: 404 ...` | The model was never downloaded | Run `ollama pull llama3.2` |
| `OpenAI request failed: ... 401` | The key is wrong or expired | Create a new key and update `.env` |
| `OpenAI request failed: ... 429` | Rate limit or no credit left | Wait a moment, or check your API account |
| `ModuleNotFoundError: No module named 'openai'` | Packages are not installed | Activate the venv and run `pip install -r requirements.txt` |
| `.\.venv\Scripts\Activate.ps1 cannot be loaded` | PowerShell script policy | Run the `Set-ExecutionPolicy` command from section 6 |

## 15. Memory is temporary

The conversation is kept in an ordinary Python list (and in
`st.session_state` for the Streamlit app). Both live only inside the running
program's memory.

That means the chatbot forgets everything when you:

- close the terminal or press `Ctrl+C`,
- type `exit` or `quit`,
- press **Clear conversation** in the Streamlit app, or
- stop and restart `streamlit run app.py`.

Nothing is written to a file or a database. If you want memory that survives a
restart, you would have to save the list to a file or a database, which is a
topic for a later project.
