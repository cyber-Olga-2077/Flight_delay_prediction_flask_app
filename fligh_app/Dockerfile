FROM python:3.12.1-slim-bookworm
WORKDIR /flask-app
COPY ./requirements.txt /flask-app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=flight_app.py
CMD ["flask", "run", "--host", "0.0.0.0"]