FROM python:3.9-slim

# WORKDIR /app

# Upgrade pip and install virtualenv
RUN pip install --upgrade pip && pip install virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment and install dependencies
COPY requirements.txt .
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]