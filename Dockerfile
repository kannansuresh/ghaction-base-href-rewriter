FROM python:3.12-slim
WORKDIR /action
COPY . .
ENTRYPOINT ["python", "action.py"]
