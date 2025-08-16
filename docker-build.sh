docker build -t sign-gen -f backend/debian-slim/Dockerfile .
docker run -it -p 8000:8000 sign-gen
