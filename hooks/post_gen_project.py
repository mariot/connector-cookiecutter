import os

REMOVE_PATHS = [
    '{% if cookiecutter.config_file != "yml file" %}src/config.yml{% endif %}',
    '{% if cookiecutter.config_file != ".env file" %}.env{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)