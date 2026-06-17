# podman01 CTF separated tasks

This repository builds separate Docker images for each CTF task and pushes them to Docker Hub.

Docker Hub repository:

```text
luvsannorovv/podman01
```

## Tags

- day2-hidden-file
- day3-env-leak
- day4-header
- day5-cookie
- day6-base64
- day7-permission
- day8-file-viewer
- day9-sqli
- day10-final

Day1 can remain as your existing tag.

## Run example

```bash
docker pull luvsannorovv/podman01:day5-cookie
docker run --rm -p 8080:8080 luvsannorovv/podman01:day5-cookie
```

Open:

```text
http://localhost:8080
```

## Required GitHub repository secrets

- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN
- CTF_SALT
