FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 git && \
    git clone https://github.com/KartikeyaReddy24/AutoBuildImage-ExtractingEmailsOnK8s.git && \
    apt-get remove -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR AutoBuildImage-ExtractingEmailsOnK8s

RUN apt-get update && \
    apt-get install -y python3-pip && \
    python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir docker PyGithub && \
    apt-get purge -y python3-pip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["python3", "/AutoBuildImage-ExtractingEmailsOnK8s/src/main.py"]



# FROM python:3.9

# RUN pip install docker PyGithub os time && \
#     git clone https://github.com/KartikeyaReddy24/AutoBuildImage-ExtractingEmailsOnK8s.git && \

# WORKDIR AutoBuildImage-ExtractingEmailsOnK8s

# RUN python3 -m pip install --no-cache-dir --upgrade pip && \
#     python3 -m pip install --no-cache-dir googlesearch-python psycopg2-binary -r requirements.txt && \

# CMD ["python3", "/AutoBuildImage-ExtractingEmailsOnK8s/src/main.py"]
