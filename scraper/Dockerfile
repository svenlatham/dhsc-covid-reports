FROM python:3.9.1-slim-buster
RUN pip install pyexcel-ods pyexcel
COPY parser.py /
COPY sources.txt /
ENTRYPOINT ["python","/parser.py"]