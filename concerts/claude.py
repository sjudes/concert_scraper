import os
from dotenv import load_dotenv
load_dotenv()
from anthropic import Anthropic


def claude_query(prompt, model='haiku'):
    client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

    model_map = {
        'sonnet': "claude-3-sonnet-20240229",
        'haiku': "claude-3-haiku-20240307",
        'opus': "claude-3-opus-20240229",
    }

    message = client.messages.create(
        model=model_map[model],
        max_tokens=4096,
        temperature=0,
        system="Concert information extractor",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    return message.content