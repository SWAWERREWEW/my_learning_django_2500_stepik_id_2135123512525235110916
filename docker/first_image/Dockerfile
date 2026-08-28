# docker\first_image\Dockerfile
FROM python:3.12-alpine
WORKDIR /python-app
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt
COPY Dockerfile .
ENV PYTHONUNBUFFERED=1
COPY for_first_image.py .
# CMD
ENTRYPOINT ["python", "for_first_image.py"]
