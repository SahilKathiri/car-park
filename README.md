To run the project:
- Download python 3.6+ and virtualenv `pip install virtualenv`
- Clone this project
- Create a virtual environment `virtualenv venv`
- Install requirements `pip install -r requirements.txt`
- Make migrations `python manage.py makemigrations`
- Migrate `python manage.py migrate`
- Run the server `python manage.py runserver`
- Create Superuser (follow prompt) `python manage.py createsuperuser`


Go to `127.0.0.1:8000/admin` for Admin portal
Go to `127.0.0.1:8000/` for Parking Lot UI
Go to `127.0.0.1:8000/stats` for Car stats
