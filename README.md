# LangChain Google Gemini Example

This project demonstrates how to use **LangChain** with **Google’s Gemini API** to build and interact with AI chat models.
It uses **`uv`** for dependency management and environment setup.

---

## 🧩 Project Overview

This simple script initializes a Gemini model via LangChain’s `init_chat_model` function and sends a message (`"Hello world!"`) to the model, then prints the AI’s response.

---

## ⚙️ Installation Guide

Follow the steps below to set up and run the project.

### 1. Initialize a new project with `uv`

```bash
uv init
```

### 2. Create and activate a virtual environment

```bash
uv venv
.venv\Scripts\activate   # For Windows
```

*(For macOS/Linux, use `source .venv/bin/activate`)*

### 3. Install dependencies

Add the required package using:

```bash
uv add "langchain[google-genai]"
```

### 4. Add your Google API Key

In your `main.py` file, replace the placeholder with your actual API key:

```python
os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"
```

Alternatively, you can store it in your environment:

```bash
setx GOOGLE_API_KEY "your_actual_api_key_here"   # Windows
export GOOGLE_API_KEY="your_actual_api_key_here" # macOS/Linux
```

---

## 🚀 Running the Script

To run your script, use:

```bash
uv run main.py
```

You should see the model’s response printed to your terminal.

---

## 📄 Example Code

```python
import os
os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
response = model.invoke([{"role": "user", "content": "Hello world!"}])
print(response.content)
```

---

## ✅ Output Example

```
Hello! How can I assist you today?
```

