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
Run project: ```http://localhost:8000/users```

## Tests
```bash
docker ps -a
```
```bash
docker exec -it $CONTAINER_ID /bin/bash
```
```bash
python3 manage.py test
```