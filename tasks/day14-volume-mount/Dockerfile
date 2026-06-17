FROM python:3.12-slim

ARG TASK_TAG=day14-volume-mount
ARG CTF_SALT=demo-salt-change-me
ENV TASK_TAG=${TASK_TAG}
ENV CTF_SALT=${CTF_SALT}

WORKDIR /opt/ctf
RUN pip install --no-cache-dir flask
COPY app.py flaggen.py ./
RUN python flaggen.py >/dev/null \
    && mkdir -p /data \
    && useradd -m ctfuser \
    && chmod 0444 /opt/ctf/flag.txt \
    && chmod 0777 /data
VOLUME ["/data"]
USER ctfuser
EXPOSE 8080
CMD ["python", "app.py"]
