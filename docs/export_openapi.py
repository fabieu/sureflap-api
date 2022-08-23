# Built-in modules
import json
from pathlib import Path

# PyPi modules

# Local modules
from sureflap_api.main import app

OPENAPI_PATH = Path(__file__).resolve().parent.parent / "public" / "openapi.json"

with open(OPENAPI_PATH, "w") as f:
    f.write(json.dumps(app.openapi()))
