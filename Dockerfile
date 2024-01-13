FROM python:3.12-slim
WORKDIR /action
COPY action.py ./
ENTRYPOINT ["python", "action.py"]
