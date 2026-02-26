#!/usr/bin/env python3
"""
Debug API connectivity tests for LiteLLM configured providers.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

try:
    import litellm
except ImportError:
    print("ERROR: litellm not installed. Install with: pip install litellm")
    sys.exit(1)

# Enable debug logging
litellm.set_verbose = True


def test_api(model: str, provider: str, max_tokens: int = 10) -> bool:
    """Test a single API endpoint with minimal token usage."""
    print(f"\n{'='*60}")
    print(f"Testing {provider}: {model}")
    print(f"{'='*60}")

    # Check env vars
    if "anthropic" in model.lower():
        api_key = os.getenv("ANTHROPIC_API_KEY", "NOT SET")
        print(f"API Key present: {bool(api_key and api_key != 'NOT SET')}")
    elif "openai" in model.lower() and "kimi" not in model.lower():
        api_key = os.getenv("OPENAI_API_KEY", "NOT SET")
        print(f"API Key present: {bool(api_key and api_key != 'NOT SET')}")
    elif "gemini" in model.lower():
        api_key = os.getenv("GOOGLE_API_KEY", "NOT SET")
        print(f"API Key present: {bool(api_key and api_key != 'NOT SET')}")
    elif "kimi" in model.lower():
        api_key = os.getenv("MOONSHOT_API_KEY", "NOT SET")
        print(f"API Key present: {bool(api_key and api_key != 'NOT SET')}")

    try:
        response = litellm.completion(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Say 'OK'",
                }
            ],
            max_tokens=max_tokens,
            timeout=30,
        )

        result = response.choices[0].message.content
        print(f"✓ SUCCESS | Response: {result[:50]}")
        print(f"  Tokens used: {response.usage.completion_tokens + response.usage.prompt_tokens}")
        return True

    except Exception as e:
        print(f"✗ FAILED | Error: {type(e).__name__}")
        print(f"  Message: {str(e)[:200]}")
        return False


def main():
    """Test all configured cheap models."""

    # Test models from the config
    test_cases = [
        ("anthropic/claude-haiku-4-5", "Anthropic Haiku"),
        ("openai/gpt-4o-mini", "OpenAI GPT-4o-mini"),
        ("gemini/gemini-2.0-flash", "Google Gemini 2.0 Flash"),
        ("openai/kimi-k2.5", "Moonshot Kimi"),
    ]

    results = {}

    print("\n🚀 LiteLLM API Connectivity Tests (Debug Mode)\n")

    for model, provider in test_cases:
        success = test_api(model, provider)
        results[provider] = success

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for provider, success in results.items():
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status} | {provider}")

    print(f"\nResult: {passed}/{total} APIs working\n")

    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
