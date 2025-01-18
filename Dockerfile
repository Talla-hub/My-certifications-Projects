FROM ubuntu

# Set working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY requirements.txt /app/
COPY . /app/
COPY Web_App/templates /app/templates

# Install required system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    python3 -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose the port your app will run on
EXPOSE 5000

# Activate the virtual environment and run the Flask app
ENTRYPOINT ["/app/venv/bin/python3"]
CMD ["-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "Web_App.project:app"]

