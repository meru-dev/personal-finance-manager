up:
	docker-compose -f docker-compose.yaml up -d --build

down:
	docker-compose -f docker-compose.yaml down --remove-orphans

restart:
	make down
	make up
