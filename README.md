# docker-container-fastapi

Build the image : 

```bash
docker build -t fastapi .
```

Run the container:

```bash
docker run -p 8001:8001 fastapi -d
```

Access application:

[http://localhost:8001/docs](http://localhost:8001/docs)