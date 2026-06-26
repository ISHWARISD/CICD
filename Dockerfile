# Start from a small official Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (so Docker can cache this layer
# and skip reinstalling deps if only app.py changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the app code
COPY . .

# Document which port the app listens on
EXPOSE 5000

# Command that runs when the container starts
CMD ["python", "app.py"]
