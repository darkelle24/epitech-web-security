FROM python:3.6

COPY requirement* requirement.txt
RUN pip install -r requirement.txt
COPY . .

EXPOSE 5000

CMD ["python3","startup.py"]
