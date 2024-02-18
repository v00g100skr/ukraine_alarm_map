FROM python:3.12.2
ADD manage.py .
ADD requirements.txt .
ADD jaam .
RUN pip install -r requirements.txt --no-cache-dir && rm -f requirements.txt
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000