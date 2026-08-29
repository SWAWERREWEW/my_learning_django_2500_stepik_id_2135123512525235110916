# docker\flask_db_image\Dockerfile
FROM python:3.12-slim
RUN groupadd -r newgroup && useradd -r -g newgroup kikidon

RUN pip install flask psycopg2-binary

EXPOSE 4000

WORKDIR /app
COPY ./flask_project/site.py .

USER kikidon
ENTRYPOINT ["python", "site.py"]
