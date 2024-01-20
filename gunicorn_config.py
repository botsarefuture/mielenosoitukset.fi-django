import multiprocessing
from protest_app.wsgi import application

# Calculate the number of workers based on CPU cores
workers = multiprocessing.cpu_count() * 2 + 1  # You can adjust the multiplier based on your needs

bind = "0.0.0.0:8000"