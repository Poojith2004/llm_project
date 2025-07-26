# Base image
FROM python:3.11-slim

# Disable .pyc files and buffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the full project
COPY . .

# Expose port only if needed (not required for CLI app)
# EXPOSE 8000

# Default command (interactive prompt)
CMD ["python", "main.py"]
