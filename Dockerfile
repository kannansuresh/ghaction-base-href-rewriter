FROM python:3.12-slim

COPY . /action
WORKDIR /action

ENTRYPOINT ["python", "/action/rewrite_base_href.py"]
