# Aerolyzer\_App

The code behind the [Aerolyzer](https://github.com/Aerolyzer/Aerolyzer) mobile web application

## Dependencies
* [Django](https://www.djangoproject.com/). To install the Django dependency:
  ```conda install django``` or ```pip install django```

## Important things to note are:
1.Postgresql 9.5.6 (min requirement) should be installed and running on port 5432. Postgresql can be downloaded [here](https://www.postgresql.org/download/).

2.The database in Postgresql should be set up with the following settings for the PostgreSql database:
```
   NAME: aerolyzer
   USER: postgres
   PASSWORD:Aerolyzer_1
```   
## Running the Aerolyzer app
To run the Aerolyzer app locally:
* ```cd Aerolyzer/```
* ```python manage.py runserver```
* Open your browser to http://127.0.0.1:8000/app/

To run the Aerolyzer app in production (using guincorn and whitenoise):
* Run the script production/run_production.sh
