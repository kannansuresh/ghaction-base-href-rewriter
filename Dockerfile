FROM python:3.12-slim
COPY . /action
WORKDIR /action
ENTRYPOINT ["python", "/action/base_href_rewriter.py"]
