# Day 14 - Volume Mount

Concept: bind mount / volume into a container.

Example:

```bash
echo do188-volume-ok > unlock.txt
podman run --rm -p 8080:8080 -v "$PWD/unlock.txt:/data/unlock.txt:ro" docker.io/luvsannorovv/podman01:day14-volume-mount
```

On SELinux enforcing systems such as RHEL/Fedora, add `:Z` or `:z` to the volume mount.
