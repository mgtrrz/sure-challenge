FROM python:3.12-slim-bullseye

RUN mkdir /app
WORKDIR /app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENV=${ENV}

# Copy requirements and install
COPY ./requirements.txt /app/
RUN python3 -m pip install -r requirements.txt

# Copy python script
COPY ./init.py /app/
COPY ./main.py /app/

CMD [ "python3", "main.py"]