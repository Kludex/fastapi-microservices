SHELL=bash
MICROSERVICES = users


.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: tests
tests:  ## Run tests
	@echo "🍜 Running tests..."
	@$(eval POD=$(shell sh -c 'kubectl get pod -l app=users -o jsonpath="{.items[0].metadata.name}"'))
	@kubectl exec $(POD) -- pytest -v tests --cov app --cov-report=term-missing:skip-covered --cov-report=xml --cov-fail-under 69


.PHONY: migrations
migrations:  ## Generate migrations - `msg` parameter is needed
	@$(eval POD=$(shell sh -c 'kubectl get pod -l app=users -o jsonpath="{.items[0].metadata.name}"'))
	$(eval OUTPUT=$(shell sh -c 'kubectl exec $(POD) -- alembic revision --autogenerate -m $(msg)'))
	$(eval CONTAINER_FILE=$(shell sh -c 'echo "$(OUTPUT)" | grep -Po "/app/migrations/versions/(\w+.py)"'))
	$(eval LOCAL_FILE=$(shell sh -c 'echo "$(CONTAINER_FILE)" | sed "s/\/app/users/g"'))
	@kubectl exec $(POD) -- cat $(CONTAINER_FILE) >> $(LOCAL_FILE)
