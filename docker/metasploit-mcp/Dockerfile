FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/GH05TCREW/MetasploitMCP.git .
RUN pip install -r requirements.txt

ENV MSF_PASSWORD=password
ENV MSF_SERVER=metasploit
ENV MSF_PORT=55553
ENV MSF_SSL=false

CMD ["python", "MetasploitMCP.py", "--transport", "http", "--host", "0.0.0.0", "--port", "8085"]
