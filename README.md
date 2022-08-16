# Reactions

### Installation using Docker

Clone my repository

```bash
git clone https://github.com/admed/reactions
```

Go to directory
```
cd reactions
```

Run docker directly
```
docker-compose build
```
```
docker-compose up
```

or by makefile commends
```
make build
```
```
make up
```
You can use Makefile commends for more options write help
```
make help
```

Got to your web browser use localhost and port 8000

[http://localhost:8000](http://localhost:8000)

You can open SWAGGER docs 

[http://localhost:8000/docs](http://localhost:8000/docs)


Try post function from SWAGGER - Try it out -> fill inputs data

### Installation for Ubuntu/Linux

---
**NOTE**

Requirements: python 3.10, pipenv and uvicorn

---

```bash
git clone https://github.com/admed/reactions
```

Go to directory
```
cd reactions
```

Next, activate the Pipenv shell:
```
pipenv shell
```

Intall dependencies
```
pipenv install
```

Run uvicorn
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

Got to your web browser use localhost and port 8000

[http://localhost:8000](http://localhost:8000)

You can open SWAGGER docs 

[http://localhost:8000/docs](http://localhost:8000/docs)


Try post function from SWAGGER- Try it out -> fill inputs data