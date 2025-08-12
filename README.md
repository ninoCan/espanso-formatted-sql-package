# Espanso formatted-sql package

## Contributions are welcomed

### Run the package validation locally

Sometimes it's useful to run the validation process locally. To do so, you have
to make the following steps:

- have python 3.12 installed and make an environment in your local folder. We
use [`uv`](https://github.com/astral-sh/uv) often, and if you don't know it yet
, you should!

```bash
uv venv --python 3.12
```

- install the `pyyaml` dependency

```bash
uv pip install pyyaml
```

- run the `main.py` *from the root folder* (because the script uses `glob` to
find what packages are in the `packages/` folder)

```bash
uv run .github/scripts/validate/main.py
```

- wait until you have the results!
