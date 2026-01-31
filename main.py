import subprocess
import sys
from pathlib import Path

app_path = Path(__file__).parent / "frontend" / "app.py"

subprocess.run([
    sys.executable,
    "-m",
    "streamlit",
    "run",
    str(app_path)
])
