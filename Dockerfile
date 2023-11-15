FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /workspace
WORKDIR /workspace
COPY ./requirements /workspace/requirements
RUN pip install -r requirements/local_build.txt
COPY . /workspace/
RUN inv project.install-requirements
