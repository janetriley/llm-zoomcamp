from openai import OpenAI
import tiktoken
import os

DEFAULT_MODEL = 'gpt-4o'
client = None
_key = os.getenv("OPENAI_API_KEY")

# make sure it's ready to go
assert _key


def get_client():
    global client
    if not client:
        client = OpenAI()
    return client


def llm(prompt):
    response = get_client().chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def count_tokens(prompt):
    encoding = tiktoken.encoding_for_model(DEFAULT_MODEL)
    return len(encoding.encode(prompt))


def completions(prompt):
    response = client.chat.completions.create(model=DEFAULT_MODEL,
                                              messages=[{'role': 'user',
                                                         'content': prompt,
                                                         }])
