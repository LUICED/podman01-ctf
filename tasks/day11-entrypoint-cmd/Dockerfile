FROM python:3.12-slim

ARG TASK_TAG=day11-entrypoint-cmd
ARG CTF_SALT=demo-salt-change-me
ENV TASK_TAG=${TASK_TAG}
ENV CTF_SALT=${CTF_SALT}

WORKDIR /opt/ctf
RUN pip install --no-cache-dir flask
COPY app.py flaggen.py ./
RUN python flaggen.py >/dev/null \
    && useradd -m ctfuser \
    && chmod 0444 /opt/ctf/flag.txt
USER ctfuser
EXPOSE 8080
ENTRYPOINT ["python", "/opt/ctf/app.py"]
CMD ["serve"]
