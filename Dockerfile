FROM python:3.8.5-alpine3.12
RUN pip3 install pygithub==1.53
COPY action.py /action.py
ENTRYPOINT ["/action.py"]