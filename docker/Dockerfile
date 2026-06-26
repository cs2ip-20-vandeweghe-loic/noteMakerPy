FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

# on copie depuis la racine (context = ..)
COPY pyproject.toml .
COPY src ./src

RUN pip install --no-cache-dir -e .

RUN mkdir -p /data

ENV NOTES_DB=/data/.notes.json
ENV NOTES_EXPORT_DIR=/data/notes
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["note"]