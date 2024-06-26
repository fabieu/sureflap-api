# Built-in modules
import json
from pathlib import Path

# Local modules
from surehub_api.main import app

# PyPi modules

OPENAPI_PATH = Path(__file__).resolve().parent.parent / "public" / "openapi.json"

with open(OPENAPI_PATH, "w") as f:
    f.write(json.dumps(app.openapi()))
