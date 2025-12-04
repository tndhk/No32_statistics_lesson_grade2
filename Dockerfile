FROM python:3.11-slim

WORKDIR /work

RUN pip install --no-cache-dir \
    marimo \
    pandas \
    numpy \
    scipy \
    matplotlib \
    seaborn \
    statsmodels

EXPOSE 2718

CMD ["marimo", "edit", "--host", "0.0.0.0", "--port", "2718", "--no-token"]
