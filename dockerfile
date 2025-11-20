# Use an official Python 3.13 image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first (faster builds)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files to container
COPY . .

# Expose port for gunicorn
EXPOSE 8000

# Start your Flask app using gunicorn
# Here, app:app = file app.py and Flask object named app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "600", "app:app"]
