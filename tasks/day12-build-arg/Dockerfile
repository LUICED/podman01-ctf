FROM python:3.12-slim

WORKDIR /opt/challenge
COPY starter/ /opt/challenge/starter/
COPY server.py /opt/challenge/server.py
RUN pip install --no-cache-dir flask && tar -czf /opt/challenge/starter.tar.gz -C /opt/challenge starter
EXPOSE 8080
CMD ["python", "/opt/challenge/server.py"]
