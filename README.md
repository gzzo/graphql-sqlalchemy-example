This is a simple example to demo [graphql-sqlalchemy](https://github.com/gzzo/graphql-sqlalchemy).

# Usage

```shell
git clone https://github.com/gzzo/graphql-sqlalchemy-example.git
cd graphql-sqlalchemy-example

poetry install
poetry run uvicorn --port 5000 --host 0.0.0.0 graphql_sqlalchemy_example.run:app
```

Now you can visit http://localhost:5000/graphql/
