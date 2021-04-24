services = ['users', 'users-worker', 'redis', 'postgres']

[k8s_yaml("k8s/%s.yaml" % service) for service in services]
docker_build('users', 'users', dockerfile='users/docker/backend.dockerfile')
docker_build('users-worker', 'users', dockerfile='users/docker/worker.dockerfile')
k8s_resource(workload="users-deployment", port_forwards="8000:80")
