# Serve static files directly by Gunicorn in production
from whitenoise import WhiteNoise
from protest_app.wsgi import application  # Replace 'your_project_name' with your actual project name

application = WhiteNoise(application, root='/static/')

workers = 3  # Adjust the number of workers based on your server's capabilities
bind = "0.0.0.0:8000"
