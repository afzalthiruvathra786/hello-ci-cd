FROM python:3.13

WORKDIR /app
COPY . /app
RUN pip install -r requirments.txt

CMD ["python", "src/app.py"]
