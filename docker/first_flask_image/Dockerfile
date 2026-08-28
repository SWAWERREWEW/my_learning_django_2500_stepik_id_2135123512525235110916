# docker\first_flask_image\Dockerfile
FROM python:3.12-slim
RUN groupadd -r newgroup && useradd -r -g newgroup kikidon
RUN pip install --no-cache-dir flask
WORKDIR /app
COPY ./flask_project/site.py .
USER kikidon
# VOLUME /app
ENTRYPOINT ["python", "site.py"]
EXPOSE 4000
