# Use an official Python runtime as a parent image
FROM python:3.9

LABEL maintainer="dimention.io"

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE server.settings

# Set the working directory in the container
WORKDIR /singularity-api

# Copy the requirements file into the container
COPY requirements.txt /singularity-api/

# Install the required packages
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /singularity-api/

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
