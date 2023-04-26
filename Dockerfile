FROM python:3.9

RUN pip install docker PyGithub os time && \
    git clone https://github.com/KartikeyaReddy24/AutoBuildImage-ExtractingEmailsOnK8s.git && \

WORKDIR AutoBuildImage-ExtractingEmailsOnK8s

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir googlesearch-python psycopg2-binary -r requirements.txt && \

CMD ["python3", "/AutoBuildImage-ExtractingEmailsOnK8s/src/main.py"]
