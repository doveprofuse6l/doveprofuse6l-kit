# doveprofuse6l-kit

Sort a folder of files into per-type subfolders.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m doveprofuse6l_kit.cli --help
```

```python
from doveprofuse6l_kit.core import Doveprofuse6lTool

tool = Doveprofuse6lTool()
print(tool)
```

## Layout

```
doveprofuse6l_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 doveprofuse6l
