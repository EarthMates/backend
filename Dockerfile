# # Use an official Python runtime as a parent image
# FROM python:3.10

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED=1

# # Django service
# ENV PORT=8080

# # Set the working directory in the container
# WORKDIR /backend

# # Copy the contents of the backend directory into the container at /backend
# COPY . /backend

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose port 8000 to the outside world
# EXPOSE 8000

# # Run manage.py when the container launches
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



FROM python:3.10.12
ENV PYTHONBUFFERED=1                    
ENV PORT 8080                           
WORKDIR /app
COPY . /app/                            
RUN pip install --upgrade pip
RUN pip install -r depl_requirements.txt     

# Run app with gunicorn command
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:"${PORT}"

EXPOSE ${PORT}                          
