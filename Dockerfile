FROM python:3.6

MAINTAINER Tyler J. Skluzacek (skluzacek@uchicago.edu) 

COPY xtract_jsonxml_main.py requirements.txt /
COPY test_files /

RUN pip install -r requirements.txt

ENV CONTAINER_VERSION=1.0

#ENTRYPOINT ["python", "xtract_jsonxml_main.py"]
