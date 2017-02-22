# Aerolyzer\_App

The code behind the [Aerolyzer](https://github.com/Aerolyzer/Aerolyzer) mobile web application 

## Dependencies
[Django](https://www.djangoproject.com/)
* To install the Django dependency:
``` conda install django``` or ```pip install django```

## Running the Aerolyzer app
To run the Aerolyzer app locally:

* ```cd Aerolyzer/```
* ```python manage.py runserver```
  
* Open your browser to http://127.0.0.1:8000/app/



To run the Aerolyzer app in production (using guincorn and whitenoise):

* Modify the settings.py file 

  ```
  cd Aerolyzer/Aerolyzer
  nano settings.py
  DEBUG = False
  ```

* If necessary, also update the ```ALLOWED_HOSTS``` tag to add your host name.

* Start the app with guincorn

  ```
  cd Aerolyzer
  gunicorn Aerolyzer.wsgi
  ```

