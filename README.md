## Installation

```bash
$ git clone https://github.com/embium/mobilizeamerica-backend-assignment
$ cd mobilizeamerica-backend-assignment
$ pip install -r requirements.txt
$ uvicorn app.main:app
```

## Usage

Create a basic URL shortened.
```bash
$ curl -s -X POST http://127.0.0.1:8000 -d '{"target": "https://google.com"}'
{
  "link": "4QiXbz8"
}
```

Redirection to the target URL, the `-L` option should be used with `curl` to follow the `302` redirection.
```bash
$ curl -s -X GET http://127.0.0.1:8000/4QiXbz8 -L
```

Get link information, this will output the `target` and `clicks` information.
```bash
$ curl -s -X GET http://127.0.0.1:8000/4QiXbz8/info
{
  "target": "http://google.com",
  "created": "2021-08-07T13:04:26.437782",
  "link": "4QiXbz8",
  "clicks": [
    {
      "created": "2021-08-07T13:05:17.337219",
      "id": 1,
      "link_id": 1
    }
  ]
}
```
List only `clicks` between a giving range
```bash
$ curl -s -X GET http://127.0.0.1:8000/4QiXbz8/info?start_date=2021-08-07&end_date=2021-08-07
{
  "target": "http://google.com",
  "created": "2021-08-07T13:04:26.437782",
  "link": "4QiXbz8",
  "clicks": [
    {
      "created": "2021-08-07T16:42:05.494924",
      "id": 1,
      "link_id": 1
    },
    {
      "created": "2021-08-07T16:43:08.836689",
      "id": 2,
      "link_id": 1
    }
  ]
}
```

Remove permanently an URL shortened from the database.
```bash
$ curl -s -X DELETE http://127.0.0.1:8000/4QiXbz8
```