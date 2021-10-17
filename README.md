# Code Challenge for Juntos Somos Mais

## Installation
1. Install Docker and Docker Compose.
2. Clone this repository or fork this repository:
```bash
git clone https://github.com/heytorvas/juntossomosmais.git
```
3. Change directory to repository:
```bash
cd juntossomosmais
```

## Development Environment
1. Build the containers:
```bash
docker-compose build
```
2. Up the containers:
```bash
docker-compose up &
```

## Notes
* Run project: ```http://localhost:8000/api/users```
* API documentation: ```http://localhost:8000/api/docs```

## Query String Paramaters /users/
* page -> number of page ```?page=1```
* size -> size of page ```?size=10```
* region -> number of page ```?region=sul```
* type -> number of page ```?type=laborious```

## Tests
Execute tests on API

1. Get all docker containers on machine and find API's container id.
```bash
docker ps -a
```
2. Enter inside on API's container.
```bash
docker exec -it $CONTAINER_ID /bin/bash
```
3. Execute the following command for execute tests.
```bash
python3 manage.py test
```