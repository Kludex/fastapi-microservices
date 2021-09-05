services = ['users', 'worker', 'redis', 'postgres', 'ingress']
yaml_files = ["k8s/%s.yaml" % service for service in services]

k8s_yaml(yaml_files)
docker_build('kludex/users', '.', dockerfile='services/users/Dockerfile')
docker_build('kludex/worker', '.', dockerfile='services/worker/Dockerfile')
k8s_resource(workload="users-deployment", port_forwards="8000:80")
