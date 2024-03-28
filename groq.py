

import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)