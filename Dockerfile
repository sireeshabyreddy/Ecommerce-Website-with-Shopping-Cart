# Step 1: Use an official Python runtime as a parent image
FROM python:3.8-slim




# Step 2: Set the working directory inside the container
WORKDIR /ecom

# Step 3: Copy the requirements file (you should create this file)
COPY requirements.txt .

# Step 4: Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code
COPY . .

# Step 6: Expose the port your Django app will run on (default is 8000)
EXPOSE 8000

# Step 7: Set the environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=ecom.settings

# Step 8: Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
