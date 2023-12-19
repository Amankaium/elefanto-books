## Books Catalog

#### How to run
```sh
# clone project
# create and activate venv
pip install -r requirements.txt
# create an .env file (like .env_example)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
#### If you need to activate user via email set environment variables in .env file:
```sh
SEND_ACTIVATION_EMAIL=True # False if you don't need to activate them with email
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='yourmail@gmail.com'
EMAIL_HOST_PASSWORD='Y0urPa55word'
EMAIL_PORT=587
```
