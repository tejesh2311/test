FROM alpine

RUN apk update 


RUN apk add --update python py-pip openssl ca-certificates && \
apk --update add --virtual build-dependencies python-dev libffi-dev && \
apk add --update openssl-dev && \
pip install --upgrade pip

RUN apk add ansible
RUN apk add nodejs  
RUN apk add yarn  
RUN apk add npm  
