FROM python:3.10

WORKDIR /app
ADD run.py .
CMD ["python", "run.py"]