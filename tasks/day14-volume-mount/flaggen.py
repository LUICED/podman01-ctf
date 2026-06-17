import hashlib
import os
from pathlib import Path

tag = os.environ.get("TASK_TAG", "dayXX")
salt = os.environ.get("CTF_SALT", "demo-salt-change-me")
digest = hashlib.sha256(f"podman01-do188:{tag}:{salt}".encode()).hexdigest()[:14]
flag = f"CTF{{podman01_do188_{tag.replace('-', '_')}_{digest}}}"
Path("/opt/ctf").mkdir(parents=True, exist_ok=True)
Path("/opt/ctf/flag.txt").write_text(flag + "\n", encoding="utf-8")
print(flag)
