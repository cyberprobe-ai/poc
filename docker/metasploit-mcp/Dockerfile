FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install uv
RUN git clone https://github.com/foolsec/vibehacker_metasploit_mcp.git .
RUN uv pip install --system .

ENV MSF_PASSWORD=password
ENV MSF_SERVER=metasploit
ENV MSF_PORT=55553

CMD ["python", "main.py"]
