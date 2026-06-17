FROM python:3.12-slim

WORKDIR /opt/ctf

RUN pip install --no-cache-dir flask

COPY app.py setup_task.py ./
COPY entrypoint.sh ./entrypoint.sh

ARG TASK_TAG=unknown-task
ARG CTF_SALT=demo-salt-change-me

ENV TASK_TAG=${TASK_TAG}

RUN CTF_SALT="${CTF_SALT}" TASK_TAG="${TASK_TAG}" python setup_task.py \
    && useradd -m ctfuser \
    && chmod +x /opt/ctf/entrypoint.sh

USER ctfuser

EXPOSE 8080

CMD ["./entrypoint.sh"]
