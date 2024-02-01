from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix="SUREFLAP",
    settings_files=["settings.yaml", ".secrets.yaml"],
    validators=[
        Validator('email', 'password', must_exist=True),
        Validator('loglevel', is_in=['critical', 'error', 'warning', 'info', 'debug', 'trace']),
    ],
)
