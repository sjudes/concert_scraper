import os
from dotenv import load_dotenv
load_dotenv()
from anthropic import Anthropic


def claude_query(prompt):
    client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        temperature=0,
        system="Concert information extractor",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    return message.content