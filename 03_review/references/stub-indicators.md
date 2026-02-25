# Stub Indicators

Universal patterns that indicate placeholder or stub code. Used by the `verification-agent` during Level 2 (substantive) checks.

## Comment Markers

```
TODO
FIXME
XXX
HACK
PLACEHOLDER
NOT IMPLEMENTED
STUB
```

Any of these in a function body suggests incomplete implementation.

## Return Patterns

Empty or meaningless returns that bypass real logic:

```javascript
return null
return undefined
return {}
return []
return ""
return 0
return false
return Promise.resolve()
```

```python
return None
pass
...  # (ellipsis as function body)
```

```ruby
nil
```

```go
return nil, nil
```

**Exception**: A function that legitimately returns an empty value (e.g., a cache miss returning `null`) is not a stub. Look at the function's purpose and whether the return is the *only* logic.

## Throw Patterns

```javascript
throw new Error('not implemented')
throw new Error('TODO')
throw new NotImplementedError()
```

```python
raise NotImplementedError
raise NotImplementedError()
```

## Placeholder Text

Strings that indicate fake data or placeholder content:

```
"lorem ipsum"
"placeholder"
"test"
"example"
"dummy"
"foo" / "bar" / "baz"
"TODO"
"TBD"
```

**Exception**: Test files may legitimately use placeholder values. Only flag these in production code.

## Hardcoded Values

Values that should come from configuration or computation:

```javascript
const API_URL = "http://localhost:3000"  // should be env var
const MAX_RETRIES = 3                     // fine if documented
const SECRET_KEY = "mysecret"             // never OK
```

Flag hardcoded secrets unconditionally. Flag hardcoded URLs and config values with a warning.

## Empty Bodies

Functions, methods, or handlers with no logic:

```javascript
function handleSubmit() {}
async function fetchData() {}
app.get('/api/users', (req, res) => {})
```

```python
def handle_submit(self):
    pass

class UserService:
    pass
```

## Detection Priority

When scanning, prioritize:
1. **Empty bodies** — strongest stub signal
2. **Throw patterns** — explicit "not done"
3. **Comment markers** — acknowledged incompleteness
4. **Return patterns** — suspicious but may be legitimate
5. **Placeholder text** — context-dependent
6. **Hardcoded values** — warnings, not always stubs
