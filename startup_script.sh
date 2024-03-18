#!/bin/bash

# Create admin user - ensure this is idempotent or checks for existence to avoid errors
flask --app main.py create-admin "$ADMIN_EMAIL" "$ADMIN_PASSWORD" "$ADMIN_NAME"

# Start the Flask application
exec flask run --host=0.0.0.0