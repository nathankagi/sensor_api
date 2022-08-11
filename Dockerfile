# 
FROM python:3.9.5

# 
WORKDIR /code

# 
# copy requirements first to build dependencies
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["source", "./venv/Scripts/activate"]
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]