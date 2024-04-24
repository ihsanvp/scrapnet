FROM python:3.10
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app /app
CMD python app.py