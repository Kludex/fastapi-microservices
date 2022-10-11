# FastAPI Microservices

> **Warning**
> I don't have the bandwidth to maintain this project. If you want to help me, please send a message on https://github.com/Kludex/fastapi-microservices/issues/71. I'll happily onboard you.

This project was highly inspired on [tiangolo/full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql/).

## About

This is a fully async [FastAPI](https://fastapi.tiangolo.com/) project.

The full stack of this project is composed by:

* [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
* [ARQ](https://arq-docs.helpmanual.io/) - Job queues and RPC in python with asyncio and redis.
* [PostgreSQL](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database
* [Redis](https://redis.io/) - An open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.
* [Tilt](https://tilt.dev/) - A multi-service dev environment for teams on Kubernetes.

## Installation

For development purposes, we're going to use [Tilt](https://tilt.dev/).
Please install it, so we can continue.

After installing the above, you should be able to run the following:

``` bash
minikube start
tilt up
```

**The project generator is under development.**

For now, you can play with the first user being `admin@admin.com` / `password` .

## Why creating this project?

I've seen a lot of projects and tutorials using FastAPI. Which is awesome, and it makes me happy!

Unfortunately, there were few that I could take as reference. 😅

The only one that I've used for that purpose for a long time was the mentioned "full-stack-fastapi-postgresql". But as the time passed, I started to have my own vision about how a FastAPI project should be organized, and which technologies should be used as recommendation.

## References

* [django-postgres-skaffold-k8s](https://github.com/ksaaskil/django-postgres-skaffold-k8s)
* [fastapi-microservice-patterns](https://github.com/fkromer/fastapi-microservice-patterns)
* [Running Flask on Kubernetes](https://testdriven.io/blog/running-flask-on-kubernetes/)
* [Add Asynchronous SQLAlchemy example](https://github.com/tiangolo/fastapi/pull/2331)
* [Asynchronous I/O (asyncio) SQLALchemy documentation](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)
* [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)
* [The inner working of ARQ](https://threeofwands.com/the-inner-workings-of-arq/)
* [How we set up a production CI workflow with GitHub actions](https://insights.project-a.com/how-we-set-up-a-production-ci-workflow-with-github-actions-cc1e2aacd9da)
* [Using GitHub to deploy kubernetes](https://insights.project-a.com/using-github-actions-to-deploy-to-kubernetes-122c653c0b09)

## License

This project is under the MIT license.
