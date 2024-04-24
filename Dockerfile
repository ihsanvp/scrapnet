FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app /app
CMD python app.py