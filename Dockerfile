FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cach-dir --upgrade -r /code/requirements.txt
COPY ./core /code/core
CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "80"]