# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /code

# Install Flask
RUN pip install Flask psycopg2-binary

# Copy the HTML files into Nginx's serve directory
COPY templates/index.html /usr/share/nginx/html/
COPY templates/api.html /usr/share/nginx/html/api/

# Copy the current directory contents into the container at /code 
COPY . /code

# Make port 5000 available to the world outside this container 
# EXPOSE 5000

# Define environment variable
ENV FLASK_APP=main.py

# Run main.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
