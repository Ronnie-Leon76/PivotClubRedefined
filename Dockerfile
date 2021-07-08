FROM python:3.9-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /pivot-club
COPY requirements.txt /pivot-club/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /pivot-club/
EXPOSE 8000
#ENTRYPOINT ["/pivot-club/entrypoint.sh"]