# Day 11 - ENTRYPOINT vs CMD

Concept: ENTRYPOINT is the fixed executable, CMD is the default argument list.

Run normally:

```bash
podman run --rm -p 8080:8080 docker.io/luvsannorovv/podman01:day11-entrypoint-cmd
```

Then inspect image config and override the CMD argument.
