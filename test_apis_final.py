#!/usr/bin/env python3
"""
Test only the configured working APIs: Anthropic, OpenAI, Moonshot
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

try:
    import litellm
except ImportError:
    print("ERROR: litellm not installed")
    sys.exit(1)


def test_api(model: str, api_base: str = None, api_key: str = None, provider: str = "") -> bool:
    """Test a single API."""
    print(f"\n{'='*60}")
    print(f"Testing {provider}: {model}")
    print(f"{'='*60}")

    try:
        kwargs = {
            "model": model,
            "messages": [{"role": "user", "content": "Say OK"}],
            "max_tokens": 10,
            "timeout": 30,
        }

        if api_base:
            kwargs["api_base"] = api_base
        if api_key:
            kwargs["api_key"] = api_key

        response = litellm.completion(**kwargs)

        result = response.choices[0].message.content
        tokens = response.usage.completion_tokens + response.usage.prompt_tokens
        print(f"✓ SUCCESS | Response: {result[:50] if result else '(empty)'}")
        print(f"  Tokens used: {tokens}")
        return True

    except Exception as e:
        print(f"✗ FAILED | {type(e).__name__}")
        print(f"  Message: {str(e)[:150]}")
        return False


def main():
    """Test the three working APIs."""

    tests = [
        (
            "anthropic/claude-haiku-4-5",
            None,
            os.getenv("ANTHROPIC_API_KEY"),
            "Anthropic Claude Haiku",
        ),
        (
            "openai/gpt-4o-mini",
            None,
            os.getenv("OPENAI_API_KEY"),
            "OpenAI GPT-4o-mini",
        ),
        (
            "openai/kimi-k2.5",
            "https://api.moonshot.ai/v1",
            os.getenv("MOONSHOT_API_KEY"),
            "Moonshot Kimi",
        ),
    ]

    results = {}
    print("\n🚀 LiteLLM API Connectivity Tests (Final)\n")

    for model, api_base, api_key, provider in tests:
        success = test_api(model, api_base, api_key, provider)
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
