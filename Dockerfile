FROM python:latest-slim
WORKDIR /action
COPY action.py ./
ENTRYPOINT ["python", "action.py"]
