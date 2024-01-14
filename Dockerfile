FROM python:3.12-slim
COPY . /action
WORKDIR /action
ENV INPUT_BASE_HREF=$base_href
ENV INPUT_HTML_PATH=$html_path
ENV INPUT_HTML_GLOB=$html_glob
ENTRYPOINT ["python", "/action/base_href_rewriter.py"]
