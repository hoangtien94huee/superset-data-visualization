FROM apache/superset:latest

# Install necessary dependencies
USER root
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    pip install sqlalchemy-trino psycopg2-binary flask_cors pyhive thrift thrift_sasl trino && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the entrypoint script and set permissions
COPY entrypoint.sh /app/entrypoint.sh 

RUN chmod +x /app/entrypoint.sh 

# Set the working directory
WORKDIR /app

# Switch back to the superset user
USER superset

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
