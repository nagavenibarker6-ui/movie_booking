FROM python:3.12-slim
WORKDIR /
COPY . . 
CMD ["python", "ticket.py"]
