
#!/bin/bash

# Wait for database to be ready
echo "Waiting for database to be ready..."
while ! nc -z postgres-superset 5432; do
  sleep 1
done

# Initialize Superset
echo "Initializing Superset..."
superset db upgrade

# Create admin user if not exists
superset fab create-admin \
    --username admin \
    --firstname Superset \
    --lastname Admin \
    --email admin@superset.com \
    --password admin || true

# Initialize Superset
superset init || true

# Start Superset
echo "Starting Superset..."
/usr/bin/run-server.sh