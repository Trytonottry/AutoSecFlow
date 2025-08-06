FROM python:3.11-slim
WORKDIR /app
COPY api api
RUN pip install -r api/requirements.txt
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]