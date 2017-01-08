# getting-started-with-docker/example1/makefile
PROJECT=getting-started-docker-example1
TAG=kenophobio/$(PROJECT) 


docker-build:
	docker build --tag $(TAG) .

docker-run:
	make docker-build
	docker run --rm --name $(PROJECT) $(TAG)

docker-shell:
	docker run --rm --interactive --tty $(TAG) /bin/sh