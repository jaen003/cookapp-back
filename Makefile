.PHONY: run
run :
	@echo "Running cookapp architecture"
	@docker-compose up --remove-orphans

.PHONY: stop
stop :
	@echo "Stopping cookapp architecture"
	@docker-compose stop