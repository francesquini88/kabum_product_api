# --- Minimalist Debian 10 ("Buster") image with python3 pre-installed --- #
FROM python:3.8.5-slim as base


# --- Build Stage for installing/compiling OS dependencies and python modules --- #
FROM base as builder

# Install Debian compile-time dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    gcc \
    g++ \
    make \
    cmake \
    libpq-dev \
    python3-dev \
  && rm -rf /var/lib/apt/lists/*

# Install python packages defined in requirements.txt under /install
COPY ./requirements.txt /requirements.txt
RUN mkdir /install
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --prefix=/install --no-cache-dir --no-warn-script-location -r requirements.txt


# --- Final Application Image with just the required dependencies and modules --- #
FROM base as application

# Install Debian runtime dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq5 \
  && rm -rf /var/lib/apt/lists/*

# Copy installed dependencies at /install from builder stage to user PATH
COPY --from=builder /install /usr/local

# Set /app as work directory and copy the project source code
WORKDIR /app
COPY ./products_api /app/products_api
COPY ./VERSION.txt /app

# Expose port 80 and run REST API with gunicorn as a manager for uvicorn ASGI server with 4 workers
EXPOSE 80
ENTRYPOINT ["gunicorn", "products_api.main:app", "-b", "0.0.0.0:80", "-w", "4", "--preload"]
