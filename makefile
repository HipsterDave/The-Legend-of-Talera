.EXPORT_ALL_VARIABLES:

SHELL=/bin/bash -o pipefail
IMAGE_REPO ?= registry.heroku.com/the-legend-of-talera/web

build:
	@pack build $(IMAGE_REPO) -b docker://jkutner/web-tty -e WEB_TTY_CMD="python main.py" --pull-policy if-not-present

push: build
	@docker push $(IMAGE_REPO)

release: push
	@heroku container:release web

bash:
	@docker run -it --entrypoint=bash $(IMAGE_REPO)

run:
	@docker run -it -p 3000:3000 $(IMAGE_REPO)

.PHONY: build push release bash run
