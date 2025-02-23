import gradio as gr
from huggingface_hub import InferenceClient
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")

def respond(
    message,
    history: list[tuple[str, str]],
    system_message,
    max_tokens,
    temperature,
    top_p,
):
    messages = [{"role": "system", "content": system_message}]

    for user_msg, bot_msg in history:
        if user_msg:
            messages.append({"role": "user", "content": user_msg})
        if bot_msg:
            messages.append({"role": "assistant", "content": bot_msg})

    messages.append({"role": "user", "content": message})

    try:
        response = ""
        for message in client.chat_completion(
            messages,
            max_tokens=max_tokens,
            stream=True,
            temperature=temperature,
            top_p=top_p,
        ):
            token = message.choices[0].delta.content
            if token:  # Check if token is not None
                response += token
                yield response
    except Exception as e:
        logger.error(f"Error during inference: {e}")
        yield "An error occurred during processing. Please try again."


demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(
            value="You are a friendly and helpful AI assistant.",
            label="System Message (Instructions for the AI)",
        ),
        gr.Slider(
            minimum=1,
            maximum=2048,
            value=512,
            step=1,
            label="Max Tokens (Maximum number of tokens in the response)",
        ),
        gr.Slider(
            minimum=0.1,
            maximum=2.0,  # Reduced max temperature for stability
            value=0.7,
            step=0.1,
            label="Temperature (Controls randomness, higher = more random)",
        ),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.95,
            step=0.05,
            label="Top-p (Nucleus Sampling, controls diversity)",
        ),
    ],
)

if __name__ == "__main__":
    demo.launch()

