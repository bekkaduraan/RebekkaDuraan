FROM python:3.11.2

ADD main.py . 

RUN pip install requests beautifulsoup4 \
    pip install numpy

ENTRYPOINT ["python", "./main.py"]

CMD ["1"]