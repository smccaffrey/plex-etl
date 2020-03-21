FROM python:3.7-alpine

#ARG COMMIT_REF
#ARG BUILD_DATE

MAINTAINER Sam McCaffrey "smccaffrey70@gmail.com"

RUN mkdir /plex-etl
WORKDIR /plex-etl
COPY Pip* /plex-etl/

#RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*

RUN pip install pipenv && \
	cd /plex-etl && \
	pipenv install

ADD . /plex-etl

EXPOSE 3002:3002

CMD ["pipenv", "run", "python", "manage.py", "prod"]

#ENV APP_COMMIT_REF=${COMMIT_REF} \
#    APP_BUILD_DATE=${BUILD_DATE}