# PostgreSQL/Tornado - Deal with massive insertions

What to choose between:
 * individual inserts,
 * multiple rows insert,
 * copy statement

## Loading tests results

The tests have been performed with 100 simulated clients.
The clients are supposed to send requests every 5 milliseconds,
every request posts 100 messages (100 items to insert).

#### Individual inserts

Every item is inserted by an individual INSERT statement.

```python
for item in items["messages"]:
    cursor.execute(
        """
        INSERT INTO items (
            message
        ) VALUES (
            %(message)s
        );
        """,
        {
            "message": item["message"]
        }
    )
```

80 RPS
PostgreSQL CPU 25%

#### One multiple rows insert 

A multiple rows INSERT statement is built and executed once.

```python
sql = "INSERT INTO items(message) VALUES "
params = {}

messages = items["messages"]
amount = len(messages)

for counter, item in enumerate(messages):
    key = "message_" + str(counter)

    sql += "(%(" + key + ")s)"
    if counter != amount - 1:
        sql += ","

    params[key] = item["message"]

sql += ";"

with self.db:
    with self.db.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor
    ) as cursor:
        cursor.execute(
            sql,
            params
        )
```

235 RPS
PostgreSQL CPU 30%

#### One copy

A data string is generated and copied into the table.

```python
values = ""
for item in items["messages"]:
    values += item["message"] + "\n"

with self.db:
    with self.db.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor
    ) as cursor:
        cursor.copy_from(
            StringIO(values),
            "items",
            columns=('message',)
        )
```

275 RPS
PostgreSQL CPU 30%

## Start the service

Start the container:

```
vagrant up
```

Connect to the container:

```
vagrant ssh
source /tmp/virtual_env35/bin/activate
```

## Interface tests

Execute the tests:

```
py.test
```

## Locust tests

```
vagrant ssh
source /tmp/virtual_env35/bin/activate
locust --host="http://localhost:8080"
```
