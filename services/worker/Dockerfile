FROM python:3.9-slim as user-base

RUN useradd --create-home user
WORKDIR /home/user
USER user

COPY ./dist/src.python.worker/binary.pex /home/user/worker.pex

CMD [ "./worker.pex"]
