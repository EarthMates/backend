# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /backend

# Copy the contents of the backend directory into the container at /backend
COPY . /backend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose port 8000 to the outside world
EXPOSE 80

# Run manage.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
