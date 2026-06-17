FROM python:3.12-slim

ARG TASK_TAG=day13-image-layer-history
ARG CTF_SALT=demo-salt-change-me
ENV TASK_TAG=${TASK_TAG}
ENV CTF_SALT=${CTF_SALT}

WORKDIR /opt/ctf
RUN pip install --no-cache-dir flask
COPY make_layer_flag.py /tmp/make_layer_flag.py
RUN python /tmp/make_layer_flag.py
RUN rm -f /tmp/flag-from-old-layer.txt /tmp/make_layer_flag.py
COPY app.py ./
RUN useradd -m ctfuser
USER ctfuser
EXPOSE 8080
CMD ["python", "app.py"]
