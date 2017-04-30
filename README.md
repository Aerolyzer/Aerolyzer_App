# Aerolyzer\_App

The code behind the [Aerolyzer](https://github.com/Aerolyzer/Aerolyzer) mobile web application

## Dependencies
* [Django](https://www.djangoproject.com/). To install the Django dependency:
  ```conda install django``` or ```pip install django```

## Important things to note are:
1.Postgresql 9.5.6 (min requirement) should be installed and running on port 5432. Postgresql can be downloaded [here](https://www.postgresql.org/download/).

The database in Postgresql should be set up with the following settings for the PostgreSql database:
```
   NAME: aerolyzer
   USER: postgres
   PASSWORD:Aerolyzer_1
```   
2.Solr 5.5.4 should be installed and running on port 8983. Solr can be downloaded [here](http://lucene.apache.org/solr/downloads.html).

Steps to run Solr locally:
- Create directories "solr-5.5.4/server/solr/aerolyzer/conf" and "solr-5.5.4/server/solr/aerolyzer/data"
- After downloading solr, place provided schema.xml and solarconfig.xml files in the "solr-5.5.4/server/solr/aerolyzer/conf" directory
- Start Solr on port 8983 (the default) with the command ```solr-5.5.4/bin/solr start```
- Create the aerolyzer core with data directory "data" and instance directory "aerolyzer" by going to the Solr Web Admin UI at http://localhost:8983/solr/#/~cores/aerolyzer -> Core Admin -> Add core
    - If errors on the Web Admin UI appear when trying to create the core due to files not existing, copy files listed in the error message from "solr-5.5.4/server/solr/configsets/data_driven_schema_configs" to "solr-5.5.4/server/solr/aerolyzer/conf"

3.Directory "installDir" must exist one directory above local "Aerolyzer_App" directory.

## Running the Aerolyzer app
To run the Aerolyzer app locally:
* ```cd Aerolyzer/```
* ```python manage.py runserver```
* Open your browser to http://127.0.0.1:8000/app/

To run the Aerolyzer app in production (using guincorn and whitenoise):
* Run the script production/run_production.sh
