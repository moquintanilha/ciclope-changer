FROM hub.furycloud.io/mercadolibre/python:3.8-mini
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENTRYPOINT [ "bash", "start.sh" ]