FROM python:3.9-slim as user-base

RUN useradd --create-home user
WORKDIR /home/user
USER user

COPY ./dist/src.python.users/binary.pex /home/user/users.pex

CMD [ "./users.pex"]
