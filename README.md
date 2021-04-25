# FastAPI Microservices - WIP 👷

This project was highly inspired on [tiangolo/full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql/).

## About

This is a fully async [FastAPI](https://fastapi.tiangolo.com/) project.

The full stack of this project is composed by:

* [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
* [ARQ](https://arq-docs.helpmanual.io/) - Job queues and RPC in python with asyncio and redis.
* [PostgreSQL](https://redis.io/) - The World's Most Advanced Open Source Relational Database
* [Redis](https://www.postgresql.org/) - An open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.
* [Tilt](https://tilt.dev/) - A multi-service dev environment for teams on Kubernetes.
* [Skaffold](https://skaffold.dev/) [Optional] - Easy and Repeatable Kubernetes Development.

## Installation

It's possible to develop either with [Skaffold](https://skaffold.dev/) or [Tilt](https://tilt.dev/).
You should check how to install either of those, but for now I recommend Tilt.

After installing the above, you should be able to run the following:

``` bash
minikube start
tilt up
```

In case you've chosen Skaffold:

``` bash
minikube start
skaffold run --port-forward
```

**The project generator is under development.**

For now, you can play with the first user being `admin@admin.com` / `password` .

## Why creating this project?

I've seen a lot of projects and tutorials using FastAPI. Which is awesome, and it makes me happy!

Unfortunately, there were few that I could take as reference. 😅

The only one that I've used for that purpose for a long time was the mentioned "full-stack-fastapi-postgresql". But as the time passed, I started to have my own vision about how a FastAPI project should be organized, and which technologies should be used as recommendation.

As a disclaimer, currently, I'm probably the [most active person in the FastAPI community](https://fastapi.tiangolo.com/fastapi-people/#experts).

## References

* [django-postgres-skaffold-k8s](https://github.com/ksaaskil/django-postgres-skaffold-k8s)
* [fastapi-microservice-patterns](https://github.com/fkromer/fastapi-microservice-patterns)
* [Running Flask on Kubernetes](https://testdriven.io/blog/running-flask-on-kubernetes/)
* [Add Asynchronous SQLAlchemy example](https://github.com/tiangolo/fastapi/pull/2331)
* [Asynchronous I/O (asyncio) SQLALchemy documentation](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)
* [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)
* [The inner working of ARQ](https://threeofwands.com/the-inner-workings-of-arq/)

## License

This project is under the MIT license.
