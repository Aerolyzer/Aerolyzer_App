#!/bin/bash
# ------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# ------------------------------------------------------------
# This script is to be run on the web server for serving Aerolyzer 
# Assumptions: 
# 	1. virutalenv (https://virtualenv.pypa.io/en/stable/) is installed
#	2. nginx (https://www.nginx.com/resources/wiki/) is installed on the websever 
#			with config files at /etc/nginx
#	3. User has sudo privileges

clear

echo "Script to run Aerolyzer app in production mode. Engage Number 1!"

APP="$PWD/.."

INST_DIR="$APP/../installDir"
    
# start aerolyzer virtual env
cd $APP/Aerolyzer
source $INST_DIR/.virtualenvs/aerolyzer/bin/activate

# install requirements
pip install -r requirements.txt
echo "Requirements installed into aerolyzer virtualenv"

# Run script to collect staticfiles
echo "Run script to generate the staticfiles"
python manage.py collectstatic

# Change DEBUG option to False
cd $APP/Aerolyzer/Aerolyzer
sed -e "s/DEBUG = True/DEBUG = False/" settings.py > settingsTemp.py
mv settingsTemp.py settings.py

# Run script to update database stuff
cd $APP/Aerolyzer
python manage.py migrate auth
python manage.py migrate

# Set up Django admin
echo "Enter Django admin credentials"
python manage.py createsuperuser
echo "Thank you for setting up the Django admin credentials"

# Kill any current gunicorn processes
if [ "$(ps -ef | grep gunicorn | grep -v grep)" ]; then
    echo "Stopping current gunicorn process"
    ps -ef | grep "gunicorn" | grep -v grep | awk '{print $2}' | xargs kill -9
fi

# Run gunicorn to deploy
cd $APP/Aerolyzer
gunicorn Aerolyzer.wsgi &

# Copy webservice config file and restart webservice
cd $APP/production
echo "working on nginx stuff"
sed -e "s~root ;~root $APP/Aerolyzer/staticfiles;~" nginx.conf > nginxTemp1.conf
sed -e "s~alias ;~alias $APP/Aerolyzer/staticfiles;~" nginxTemp1.conf > nginxTemp.conf
sudo mv $APP/production/nginxTemp.conf  /etc/nginx/sites-enabled/nginx.conf
rm nginxTemp1.conf
sudo /etc/init.d/nginx restart

echo "Success completion of script. We out fam!"
exit

