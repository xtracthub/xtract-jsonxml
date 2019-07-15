FROM python:latest

MAINTAINER Ryan Wong

COPY xtract_jsonxml_main.py /

RUN pip install xmltodict statistics argparse

ENTRYPOINT ["python", "xtract_jsonxml_main.py"]