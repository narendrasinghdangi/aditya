
### The following commands are written for Ubuntu and may be different when using Windows.

## Getting started

```
cd existing_repo
git remote add origin https://github.com/narendrasinghdangi/aditya
git branch -M main
git push -uf origin main
```

1. **Activate your virtual environment** (if not already):


```bash
# Install uv if you haven't already
pip install uv

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv sync
```

After this, you can **run the server**:
```bash
bash ./entrypoint.sh
```