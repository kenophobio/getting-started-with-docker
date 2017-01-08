PROJECT=getting-started-docker-example1
TAG=kenophob.io/$(PROJECT) 


docker-build:
	docker build --tag $(TAG) .

docker-run:
	make docker-build
	docker run --rm --name $(PROJECT) $(TAG)

docker-shell:
	docker run --rm --interactive --tty $(TAG) /bin/sh