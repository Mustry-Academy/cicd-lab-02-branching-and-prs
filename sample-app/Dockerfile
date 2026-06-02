FROM python:3.12-slim

WORKDIR /app

# Runtime deps only — the test toolchain (pytest, fakeredis) stays out of the image.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Don't run as root.
RUN useradd --create-home --uid 10001 appuser
USER appuser

EXPOSE 5050

CMD ["python", "app.py"]
