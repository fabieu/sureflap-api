
from dynaconf import Dynaconf, Validator

# Default configuration variables
ENDPOINT = "https://app.api.surehub.io"
LOGLEVEL = "warning"
PORT = 3001


settings = Dynaconf(
    envvar_prefix="SUREFLAP",
    load_dotenv=True,
    validators=[
        Validator('EMAIL', 'PASSWORD', must_exist=True),
        Validator('LOGLEVEL', is_in=['critical', 'error', 'warning', 'info', 'debug', 'trace'], default="info"),
        Validator("ENDPOINT", default=ENDPOINT),
        Validator("PORT", default=PORT),
        Validator("CORS", default=None),
    ],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
