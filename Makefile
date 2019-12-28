WEB_APP := elython

build: docker.stop docker.down docker.build docker.start
start: docker.start                                                                                                   
stop: docker.stop

demo.start:
	docker-compose exec application iex --name ex@127.0.0.1 --cookie COOKIE

demo.send_message:
	docker-compose exec -e PYRLANG_ENABLE_LOG_FORMAT=1 -e PYRLANG_LOG_LEVEL=DEBUG application python3 demo.py

app.setup:                                                                                         
	docker-compose exec application sh -c 'cd /app/apps/$(WEB_APP)/assets/ && npm install'

docker.bash:
	docker-compose exec application bash

docker.build:
	docker-compose build --force-rm
	docker-compose up --detach
	docker-compose exec application pip3 install git+https://github.com/Pyrlang/Term@master --user
	docker-compose exec application pip3 install git+https://github.com/Pyrlang/Pyrlang@master --user

docker.down:
	docker-compose down --volumes

docker.start:
	docker-compose up --detach  

docker.stop:
	docker-compose stop