# ---- Base image (small + fast) ----
FROM python:3.11-slim

# ---- Environment ----
ENV PYTHONDONTWRITEBYTECODE=1 \
   PYTHONUNBUFFERED=1 \
   PORT=8080

# ---- Working directory ----
WORKDIR /app

# ---- System deps (minimal) ----
RUN apt-get update && apt-get install -y --no-install-recommends \
   gcc \
&& rm -rf /var/lib/apt/lists/*

# ---- Python deps ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- App code ----
COPY . .
# ---- Cloud Run requires 0.0.0.0 and $PORT ----
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8080"]