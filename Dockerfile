FROM python:3.6.10-alpine3.10
RUN pip3 install pygithub==1.47
COPY action.py /action.py
ENTRYPOINT ["/action.py"]