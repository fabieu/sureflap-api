from dynaconf import Dynaconf, Validator

# Default configuration variables
ENDPOINT = "https://app-api.production.surehub.io"
LOGLEVEL = "info"
PORT = 3001

settings = Dynaconf(
    envvar_prefix="SUREFLAP",
    load_dotenv=True,
    validators=[
        Validator('EMAIL', 'PASSWORD', must_exist=True),
        Validator('LOGLEVEL', is_in=['critical', 'error', 'warning', 'info', 'debug', 'trace'], default=LOGLEVEL),
        Validator("ENDPOINT", default=ENDPOINT),
        Validator("PORT", default=PORT),
        Validator("CORS", default=None),
        Validator("DEBUG", default=False),
    ],
)
