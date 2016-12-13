FROM python:3-onbuild

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY app.py /
COPY controllers /controllers
COPY swagger /swagger

EXPOSE 8080
WORKDIR /
CMD python app.py

