FROM python:3.4
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN mkdir /code
VOLUME /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install --upgrade --user awscli
RUN python
ADD . /code/
ENTRYPOINT [ "/code/bin/docker-entrypoint.sh" ]
