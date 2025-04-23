# Directories
SRC_DIR = src
DATA_DIR = data
DOC_DIR = docs

# Filenames
APP_NAME = main.py
DOCKERFILE = Dockerfile
REQUIREMENTS = requirements.txt

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  make build     - Build the Docker image"
	@echo "  make run       - Run the app inside Docker"
	@echo "  make clean     - Remove Docker image and containers"
	@echo "  make freeze    - Update requirements.txt with current env"
	@echo "  make tree      - Show project structure up to depth 3"

.PHONY: build
build:
	docker build -t $(APP_NAME) -f $(DOCKERFILE) .

.PHONY: run
run:
	docker run --rm -v $(PWD)/$(DATA_DIR):/app/$(DATA_DIR) $(APP_NAME)

.PHONY: clean
clean:
	docker rmi -f $(APP_NAME) || true

.PHONY: freeze
freeze:
	pip freeze > $(REQUIREMENTS)

.PHONY: tree
tree:
	tree -L 3