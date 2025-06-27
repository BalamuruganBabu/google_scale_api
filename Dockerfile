# Base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port Flask will run on
EXPOSE 5000

# Run the app using gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
 
