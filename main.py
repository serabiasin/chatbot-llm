import gradio as gr

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

from src.claude import *


if __name__ == "__main__":
    gr.ChatInterface(
    fn=call_llm, 
    type="messages"
).launch(    share=False)
