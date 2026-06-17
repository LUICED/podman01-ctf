import hashlib
import os
from pathlib import Path

tag = os.environ.get("TASK_TAG", "day13-image-layer-history")
salt = os.environ.get("CTF_SALT", "demo-salt-change-me")
digest = hashlib.sha256(f"podman01-layer:{tag}:{salt}".encode()).hexdigest()[:14]
flag = f"CTF{{podman01_do188_image_layer_{digest}}}"
Path("/tmp/flag-from-old-layer.txt").write_text(flag + "\n", encoding="utf-8")
