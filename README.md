# mypy-silent

Automatically add or remove `# type: ignore` commends to silence [mypy](https://github.com/python/mypy). Inspired by [pylint-silent](https://github.com/udifuchs/pylint-silent/)

## Why?

Imagine you want to add type check for a legacy code base which has thounds of exisiting mypy errors.
Instead of trying to fix all the exisiting errors, `mypy-silent` allows you to ignore the exisiting errors and adopt type checking right now.

Although the exisiting errors are ignored, all the new code are type checked -- so you can moving towards fully type checked step by step.

## Install & Usage
WARNING: `mypy-silent` modifies files **in place**. You should use some version control system ( like git ) to prevent losing codes.
```bash
pip install mypy-silent

mypy . # Whoa, lots of type error!
mypy . | mypy-silent # mypy-silent will add or remove `# type: ignore` commends to your code
mypy . # mypy should report 0 errors now.
```

## Changelog

### v0.2.1

- Fix import error on Python < 3.8

### v0.2.0

- Support parsing mypy >=0.900 messages

### v0.1.0

- Initial release
