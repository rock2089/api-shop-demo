#!/usr/bin/env python3
"""
AI Unit Test Generator — Auto-generate pytest tests from source code
=====================================================================
Drop in any Python source file, get production-ready pytest test cases.
Detects functions, classes, edge cases, and generates comprehensive tests.

API Shop: https://shop.pricepulseapi.site
Hire me: https://freelancer.com/get/rocks081?f=give
Author: @rock2089
"""

import requests
import json
import sys
import os
import ast
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================

# Get API key from env or use demo key
API_KEY = os.environ.get("API_SHOP_KEY", "YOUR_API_KEY")
API_URL = "https://pricepulseapi.site/v1/chat/completions"
MODEL = "deepseek-v4-pro"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# ============================================================
# CODE ANALYSIS
# ============================================================

def extract_functions(source_code: str) -> list[dict]:
    """Parse Python source and extract function/class signatures."""
    tree = ast.parse(source_code)
    items = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            args = [a.arg for a in node.args.args]
            decorators = [
                d.id if isinstance(d, ast.Name) else d.func.id if isinstance(d, ast.Attribute) else None
                for d in node.decorator_list
            ]
            decorators = [d for d in decorators if d]

            # Find the parent class if any
            parent = None
            for p in ast.walk(tree):
                if isinstance(p, ast.ClassDef) and node in [n for n in ast.walk(p)]:
                    parent = p.name
                    break

            items.append({
                "name": node.name,
                "args": args,
                "decorators": decorators,
                "parent_class": parent,
                "lineno": node.lineno
            })

    return items


def read_source(path: str) -> str:
    """Read source file, handling relative and absolute paths."""
    p = Path(path)
    if not p.exists():
        print(f"❌ File not found: {path}")
        sys.exit(1)
    return p.read_text(encoding="utf-8")


# ============================================================
# AI TEST GENERATION
# ============================================================

def generate_tests(source_code: str, filepath: str) -> str:
    """Use AI to generate comprehensive pytest tests."""
    functions = extract_functions(source_code)

    if not functions:
        return "# No functions found in source file.\n"

    func_list = "\n".join(
        f"  - {f['name']}({', '.join(f['args'])})"
        + (f" [decorators: {', '.join(f['decorators'])}]" if f['decorators'] else "")
        + (f" (method of {f['parent_class']})" if f['parent_class'] else "")
        for f in functions
    )

    prompt = f"""You are a senior Python developer writing pytest unit tests.

Source file: {filepath}
Functions found:
{func_list}

Full source code:
```python
{source_code[:4000]}
```

Generate a complete, production-ready pytest test file with:

1. **Imports** — pytest, the module, any needed fixtures
2. **Fixtures** — sample data, mock objects, setup helpers
3. **Test cases** — for EACH function:
   - Happy path (normal input)
   - Edge cases (empty, None, boundary values)
   - Error cases (invalid input types)
   - At least 2-3 test functions per source function
4. **Parametrized tests** — where applicable
5. **Mock external dependencies** — use unittest.mock where needed
6. **Docstrings** — clear descriptions on all test functions

Requirements:
- Use ONLY pytest (no unittest.TestCase)
- Follow AAA pattern (Arrange, Act, Assert)
- Use descriptive test names: test_<function>_<scenario>
- Add a conftest.py fixture suggestion at the top as a comment if needed

Output ONLY the Python code, no explanation before or after."""

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 4096
    }

    print(f"🧪 Generating tests for {len(functions)} functions...")
    print(f"   Functions: {', '.join(f['name'] for f in functions)}")
    print()

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        tests = data["choices"][0]["message"]["content"]

        # Clean up markdown code fences if present
        tests = tests.strip()
        if tests.startswith("```python"):
            tests = tests[tests.index("\n") + 1:]
        if tests.endswith("```"):
            tests = tests[:-3].strip()

        return tests
    except requests.exceptions.RequestException as e:
        print(f"❌ API error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Response: {e.response.text[:500]}")
        sys.exit(1)


# ============================================================
# MAIN
# ============================================================

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("Usage:   python unit_test_generator.py <source_file.py> [output_file]")
        print("Example: python unit_test_generator.py ../calculator.py tests/test_calculator.py")
        print()
        print("Set API_SHOP_KEY env var or edit API_KEY in the script.")
        print("Get your key: https://shop.pricepulseapi.site")
        sys.exit(0)

    source_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    # Read source
    source_code = read_source(source_path)
    print(f"📖 Read {len(source_code)} chars from {source_path}")

    # Generate tests
    tests = generate_tests(source_code, source_path)

    # Output
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(tests, encoding="utf-8")
        print(f"\n✅ Tests written to {output_path}")
        print(f"   Run: pytest {output_path} -v")
    else:
        print("\n" + "=" * 60)
        print(tests)
        print("=" * 60)


if __name__ == "__main__":
    main()

