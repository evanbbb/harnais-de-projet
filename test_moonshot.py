#!/usr/bin/env python3
"""Quick test of Moonshot API."""

import os
from dotenv import load_dotenv

load_dotenv()

try:
    import litellm
except ImportError:
    print("ERROR: litellm not installed")
    exit(1)

api_key = os.getenv("MOONSHOT_API_KEY")
if not api_key:
    print("ERROR: MOONSHOT_API_KEY not set")
    exit(1)

print("Testing Moonshot Kimi API...")
print("=" * 60)

try:
    response = litellm.completion(
        model="openai/kimi-k2.5",
        api_base="https://api.moonshot.ai/v1",
        api_key=api_key,
        messages=[{"role": "user", "content": "Say OK"}],
        max_tokens=10,
    )

    print(f"✓ SUCCESS")
    print(f"Response: {response.choices[0].message.content}")
    print(f"Tokens: {response.usage.completion_tokens + response.usage.prompt_tokens}")

except Exception as e:
    print(f"✗ FAILED")
    print(f"Error: {type(e).__name__}")
    print(f"Message: {str(e)[:200]}")
