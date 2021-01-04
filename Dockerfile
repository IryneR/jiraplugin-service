FROM python:3
WORKDIR /src/api
COPY api.py .
CMD ["python", "/api.py"]