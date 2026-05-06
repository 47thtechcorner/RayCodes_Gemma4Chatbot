import gradio as gr
import ollama

MODEL = "gemma4:e2b"

def chat(message, history):
    """
    message is a dict containing 'text' (str) and 'files' (list of file paths).
    history is a list of tuples: [[user_msg, bot_msg], ...]
    """
    # Extract text prompt and image paths
    prompt = message.get("text", "")
    images = message.get("files", [])
        
    messages = []
    
    # Reconstruct history for context
    for item in history:
        if isinstance(item, dict):
            # Gradio 5+ format: list of dictionaries
            content = item.get("content", "")
            if isinstance(content, (tuple, list)): 
                content = "" # Ignore media
            messages.append({"role": item.get("role", "user"), "content": str(content)})
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            # Gradio 4 format: list of tuples [user_msg, bot_msg]
            user_msg, bot_msg = item
            messages.append({"role": "user", "content": str(user_msg) if not isinstance(user_msg, tuple) else ""})
            messages.append({"role": "assistant", "content": str(bot_msg)})
        
    # Build current user message
    current_msg = {"role": "user", "content": prompt}
    if images:
        current_msg["images"] = images  # Ollama client accepts a list of file paths
    messages.append(current_msg)

    # Call Ollama with streaming enabled
    response_gen = ollama.chat(model=MODEL, messages=messages, stream=True)
    
    # Yield streamed response for real-time typing effect
    partial_message = ""
    for chunk in response_gen:
        partial_message += chunk['message']['content']
        yield partial_message

# Build minimal multimodal ChatInterface
demo = gr.ChatInterface(
    fn=chat,
    multimodal=True,
    title="Gemma 4 E2B Local Chat",
    description="A lightning-fast multimodal chatbot powered by Ollama."
)

if __name__ == "__main__":
    demo.launch()
