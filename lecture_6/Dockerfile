FROM python:3.12-slim

WORKDIR /app

#installing requirements
RUN pip install fastapi uvicorn sqlalchemy

COPY book_api ./book_api

EXPOSE 8000

CMD ["uvicorn", "book_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
