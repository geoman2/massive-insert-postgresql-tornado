# Massive INSERT in PostgreSQL through Tornado

### Start the service

Start the container:

```
vagrant up
```

Connect to the container:

```
vagrant ssh
source /tmp/virtual_env35/bin/activate
```

### Interface tests

Execute the tests:

```
py.test
```

### Locust tests

```
vagrant ssh
source /tmp/virtual_env35/bin/activate
locust --host="http://localhost:8080"
```
