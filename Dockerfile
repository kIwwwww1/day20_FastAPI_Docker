FROM python:3.13.5

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]


# как запустить 

# docker build -t my_f_image .                          
# docker run --name=first_image -p 1252:8000  my_f_image
