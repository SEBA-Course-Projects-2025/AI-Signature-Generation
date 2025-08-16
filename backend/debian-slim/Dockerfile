FROM debian:stable-slim

RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-dev \
    python3-pip \
    sqlite3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
#    && python -m pip install --upgrade pip --break-system-packages

RUN pip install --break-system-packages \
    numpy \
    uvicorn \
    torch \
    fastapi
    # coming soon

WORKDIR /app

COPY ./backend/app/ /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]