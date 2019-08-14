FROM python:3.6

MAINTAINER Ryan Wong

COPY xtract_jsonxml_main.py requirements.txt /

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/Parsl/parsl git+https://github.com/DLHub-Argonne/home_run

#ENTRYPOINT ["python", "xtract_jsonxml_main.py"]
