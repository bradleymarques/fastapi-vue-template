# Template for FastAPI and Vue.js Projects

Based off the tutorial [here](https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/).

## Running the Stack Locally

Simply run the following in the root project directory:

```sh
docker compose up --build
```

This will start the following:

+ [http://localhost:5000/](http://localhost:5000/) - Fast API backend
+ [http://localhost:8080/](http://localhost:8080/) - Vue.js frontend
+ [http://localhost:5434/](http://localhost:5434/) - PostgresDatabase (exposed for easy access with PGAdmin tools)

## First time database setup

```sh
docker-compose exec backend aerich init-db
docker-compose exec backend aerich migrate
docker-compose exec backend aerich upgrade
```
