# Gemma 4 E2B Local Chatbot

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
