import hashlib
import os
import sqlite3
from pathlib import Path

task_tag = os.environ.get("TASK_TAG", "unknown-task")
salt = os.environ.get("CTF_SALT") or "demo-salt-change-me"

tag_safe = task_tag.replace("-", "_").replace("/", "_")
digest = hashlib.sha256(f"podman01:{task_tag}:{salt}".encode()).hexdigest()[:12]
flag = f"CTF{{podman01_{tag_safe}_{digest}}}"

def write(path: str, content: str, mode: int = 0o644):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content + "\n", encoding="utf-8")
    p.chmod(mode)

if task_tag == "day2-hidden-file":
    write("/opt/ctf/.hidden/flag.txt", flag)
    write("/opt/ctf/readme.txt", "The flag is hidden somewhere under /opt/ctf.")

elif task_tag == "day3-env-leak":
    write("/opt/ctf/.flag-env", flag, 0o644)

elif task_tag in ["day4-header", "day5-cookie", "day6-base64", "day10-final"]:
    write("/opt/ctf/flag.txt", flag)

elif task_tag == "day7-permission":
    write("/opt/ctf/restricted/flag.txt", flag, 0o600)
    write("/opt/ctf/backup/.flag_backup", flag, 0o644)
    write("/opt/ctf/backup/note.txt", "A readable backup file exists somewhere under /opt/ctf.")

elif task_tag == "day8-file-viewer":
    write("/opt/ctf/public/welcome.txt", "Welcome. Only public files should be readable here.")
    write("/opt/ctf/private/flag.txt", flag, 0o644)

elif task_tag == "day9-sqli":
    db_path = Path("/opt/ctf/app.db")
    if db_path.exists():
        db_path.unlink()
    db = sqlite3.connect(str(db_path))
    cur = db.cursor()
    cur.execute("CREATE TABLE users (username TEXT, password TEXT, role TEXT)")
    cur.execute("CREATE TABLE secrets (name TEXT, value TEXT)")
    cur.execute("INSERT INTO users VALUES ('guest', 'guest', 'guest')")
    cur.execute("INSERT INTO users VALUES ('admin', 'not-the-password', 'admin')")
    cur.execute("INSERT INTO secrets VALUES ('flag', ?)", (flag,))
    db.commit()
    db.close()
    db_path.chmod(0o644)

write("/opt/ctf/task-info.txt", f"tag={task_tag}\n")
print(f"Prepared {task_tag}")
