import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)

def call_llm(message, history):
    with client.messages.stream(
        max_tokens=8096,
        messages=[{"role": "user", "content": message}],
        model="claude-3-7-sonnet-20250219",
    ) as stream:
        buffer=""
        for text in stream.text_stream:
            print(text, end="", flush=True)
            buffer=buffer+text
            yield buffer
