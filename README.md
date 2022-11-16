# Jets with Flask

Zoom zoom Zoom
---

### API GET Endpoints

```
http://127.0.0.1:9000/jet/

```

##### Response:

```
[
  {
    "id": Number
    "introduction": Number,
    "manufacturer": String,
    "name": String,
    "numberBuilt": Number,
    "status": String,
  }
  ...
]
```

#### Request with a species parameter, ie. ID

```
http://127.0.0.1:9000/jet/1
```

##### Response:

```
  {
    "id": Number
    "introduction": Number,
    "manufacturer": String,
    "name": String,
    "numberBuilt": Number,
    "status": String,
  }
```
---

### The rest of the CRUD's function

#### To create:  (Use postman for Body)

```
http://127.0.0.1:9000/jet/

```

#### Update, or Delete: (Target ID)
```
http://127.0.0.1:9000/jet/1

```
