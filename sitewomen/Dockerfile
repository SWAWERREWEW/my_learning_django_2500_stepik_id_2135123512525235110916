# sitewomen\Dockerfile

FROM python:3.12-slim
RUN groupadd -r newgroup && useradd -r -g newgroup kikidon

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/www/sitewomen
COPY req.txt .
RUN pip install -r req.txt

COPY . .
USER kikidon
