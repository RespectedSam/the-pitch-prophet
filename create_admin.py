import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pitch_prophet_project.settings') # Change this if your settings folder name is different
django.setup()

from django.contrib.auth.models import User

# Replace 'admin' and 'yourpassword123' with what you want to use!
username = 'Respect'
email = 'basseysamuel3698@gmail.com'
password = 'python777' 

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("🚀 Admin superuser created successfully on the new database!")
else:
    print("Admin user already exists.")