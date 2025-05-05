import subprocess
from functools import lru_cache


@lru_cache(maxsize=1)
def get_npm_root() -> str:
    result = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Failed to get npm root: {result.stderr.strip()}")
    return result.stdout.strip()
