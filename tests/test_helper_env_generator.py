import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
APP_ROOT = PROJECT_ROOT / "app"

for candidate in (str(APP_ROOT), str(PROJECT_ROOT)):
    if candidate not in sys.path:
        sys.path.insert(0, candidate)

# Seed minimal required env vars so EpicSettings can initialize without secrets
os.environ.setdefault("GEMINI_API_KEY", "test")
os.environ.setdefault("EPIC_EMAIL", "test@example.com")
os.environ.setdefault("EPIC_PASSWORD", "test-password")

from settings import EpicSettings
from env_generator import generate_env_example_merged


def test_env_generator():
    current_dir = Path(__file__).parent
    output_dir = Path(__file__).parent

    launch_names = ["examples", "docker", "tests"]
    for name in launch_names:
        if current_dir.joinpath(name).is_dir():
            output_dir = current_dir.joinpath(name)
        elif current_dir.parent.joinpath(name).is_dir():
            output_dir = current_dir.parent.joinpath(name)

        generate_env_example_merged([EpicSettings], output_dir=output_dir)
