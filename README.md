# Gemma 4 E2B Local Chatbot

Codes for my Youtube Video [https://youtu.be/lIms8UedInw]

A fast, local multimodal AI chatbot using the new Gemma 4 E2B model, powered by Ollama and Gradio.

## Tech Stack
- **Python**: Core logic
- **Ollama**: Local LLM execution
- **Gradio**: Web UI for multimodal chat

## Setup Instructions

1. **Install Ollama**: If you haven't already, download and install [Ollama](https://ollama.com/).
2. **Update / Pull the Model**: To get the model (or update it to the latest version), open your terminal and run:
   ```bash
   ollama pull gemma4:e2b
   ```
3. **Install Dependencies**: Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To launch the web UI, run:
```bash
python app.py
```
Then, open the local URL provided in your terminal (usually `http://127.0.0.1:7860`).

## How it works
`app.py` sets up a web interface using `gradio.ChatInterface` configured with `multimodal=True` so you can upload images along with text. The `chat` function extracts the text prompt and any attached image paths. These are then formatted into an Ollama compatible message dictionary and sent to the local `ollama` daemon. We use `stream=True` to yield chunks back to Gradio, creating a real-time typing effect.

## Test Prompts

### Image Analysis (Upload the Chart Image):

Prompt: "What continent has the largest population according to this chart? Answer in one sentence."

### OCR/Vision (Upload the Handwriting Image):

Prompt: "Transcribe the first sentence of this handwritten note exactly."

### Code Generation (Text Only):

Prompt: "Write a Python function to reverse a string. No explanations, just the code."

### Document/Structure (Text Only):

Prompt: "Write a 3-point bulleted meeting agenda for a new software project kickoff."

### Logic/Reasoning (Text Only):

Prompt: "If I have 5 apples, eat 2, and buy 3 more, how many do I have? Be as brief as possible."
