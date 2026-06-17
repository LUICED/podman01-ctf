# DO188 Advanced CTF Add-on: Day11-Day15

These tasks extend the existing `luvsannorovv/podman01` CTF with Red Hat DO188-style container concepts.

## Tags

| Tag | Difficulty | Main concept |
|---|---:|---|
| `day11-entrypoint-cmd` | 5/10 | ENTRYPOINT vs CMD, runtime command override |
| `day12-build-arg` | 5/10 | Containerfile ARG, build arguments |
| `day13-image-layer-history` | 7/10 | Image layers, deleted secrets in lower layers |
| `day14-volume-mount` | 5/10 | Bind mount / volume |
| `day15-network-sidecar` | 7/10 | Podman network, container DNS name, sidecar pattern |

## Participant command pattern

```bash
podman pull docker.io/luvsannorovv/podman01:<tag>
podman run --rm -p 8080:8080 docker.io/luvsannorovv/podman01:<tag>
```

For network/volume/build tasks, the landing page gives the first hint.

## Organizer upload

Upload these folders into your existing `podman01-ctf` GitHub repository:

```text
tasks/day11-entrypoint-cmd
tasks/day12-build-arg
tasks/day13-image-layer-history
tasks/day14-volume-mount
tasks/day15-network-sidecar
.github/workflows/docker-build-push-do188-advanced.yml
```

GitHub Secrets required:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
CTF_SALT
```
