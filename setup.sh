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
# This script is used to install all the dependency programs

clear

echo "Script to setup Aerolyzer environment."
echo "This script assumes JAVA verion 7 or higher, pip and Python 2.7.9 are installed."
echo " Engage number 1!"

APP="$PWD"

INST_DIR="$APP/../installDir"
if [ ! -d $INST_DIR ]; then
  mkdir $INST_DIR
fi
cd $INST_DIR

# Check for installation machine distro and package manager

APT_GET_CMD=$(which apt-get)
BREW_CMD=$(which brew)
YUM_CMD=$(which yum)

DISTRO_VER=$(uname -v)
DISTRO_LONG=(${DISTRO_VER//;/ })
if [[ $DISTRO_LONG =~ .*Ubuntu* ]]; then
   DISTRO="Ubuntu"
elif [[ $DISTRO_LONG =~ .*Darwin* ]]; then
   DISTRO="Darwin"
elif [[ $DISTRO_LONG =~ .*Debian* ]]; then
   DISTRO="Debian"
fi

# install PostgreSQL
if [ ! -z $APT_GET_CMD ]; then
  sudo $APT_GET_CMD install postgresql postgresql-contrib
  sudo $APT_GET_CMD install python-psycopg2
  sudo $APT_GET_CMD install libpq-dev

  echo "configure PostgreSQL"
  # configure PostgreSQL
  sudo -u postgres bash -c "psql postgres -c \"CREATE DATABASE aerolyzer\""
  sudo -u postgres bash -c "psql postgres -c \"ALTER USER postgres WITH PASSWORD 'Aerolyzer_1'\""

elif [[ ! -z $YUM_CMD ]]; then
	sudo $YUM_CMD install postgresql
elif [ $DISTRO == "Darwin" ]; then
	if [ -z $BREW_CMD ]; then
		sudo /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	fi
	$BREW_CMD update
	$BREW_CMD doctor
  $BREW_CMD install postgresql
  # $BREW_CMD cleanup PostgreSQL
  # make DB
  # initdb /usr/local/var/aerolyzer -E utf8
  # $BREW_CMD services start postgresql
  # postgres -D /usr/local/var/postgres
  sudo -u postgres bash -c "psql postgres -c \"CREATE DATABASE aerolyzer\""
  sudo -u postgres bash -c "psql postgres -c \"ALTER USER postgres WITH PASSWORD 'Aerolyzer_1'\""
else
    echo "Error: Cannot identify package manager, thus cannot install PostgreSQL. Exiting!!!!!"
    exit 1;
 fi

# echo "configure PostgreSQL"
# # configure PostgreSQL
# sudo -u postgres bash -c "psql postgres -c \"CREATE DATABASE aerolyzer\""
# sudo -u postgres bash -c "psql postgres -c \"ALTER USER postgres WITH PASSWORD 'Aerolyzer_1'\""

echo "end that config"
exit 1
# # solr stuff
# if [ ! -d "$INST_DIR/solr-5.5.4" ]; then
#   wget http://archive.apache.org/dist/lucene/solr/5.5.4/solr-5.5.4.tgz
#   tar -xvzf solr-5.5.4.tgz
#   rm solr-5.5.4.tgz
# fi

# # configure Solr and start
# if [ ! -d "$INST_DIR/solr-5.5.4/server/solr/aerolyzer" ]; then
#   mkdir solr-5.5.4/server/solr/aerolyzer
#   mkdir solr-5.5.4/server/solr/aerolyzer/data
#   cp -R solr-5.5.4/server/solr/configsets/data_driven_schema_configs/conf solr-5.5.4/server/solr/aerolyzer
#   cp $APP/schema.xml solr-5.5.4/server/solr/aerolyzer/conf
#   cp $APP/solrconfig.xml -5.5.4/server/solr/aerolyzer/conf
# fi

# # start Solr
# $INST_DIR/solr-5.5.4/bin/solr start

# # update Solr index every hr
# crontab -l > $INST_DIR/mycron
# echo "0 * * * * $APP/Aerolyzer/manage.py update_index" >> $INST_DIR/mycron
# crontab $INST_DIR/mycron
# rm $INST_DIR/mycron

if [ ! -d "$INST_DIR/.virtualenvs/" ]; then
  mkdir $INST_DIR/.virtualenvs/
fi

if [ ! -d "$INST_DIR/.virtualenvs/aerolyzer" ]; then
  cd $INST_DIR/.virtualenvs/
  if [ ! -z $(which virtualenv) ]; then
    virtualenv aerolyzer
  else
    pip install virtualenvs
  fi
  
  echo "Virtualenv env created at $INST_DIR/.virtualenvs/aerolyzer"
fi
    
# start aerolyzer virtual env
source $INST_DIR/.virtualenvs/aerolyzer/bin/activate
cd $APP/Aerolyzer

# install requirements
pip install -r requirements.txt
echo "Requirements installed into aerolyzer virtualenv"
source deactivate

echo "Successful setup environment for Aerolyzer App."
echo "**********************************************************"
echo "Please choose option to deploy Aerolyzer App: "
read -p "1 - in local mode   OR    2 - production mode ": mode
if [ $mode = "1" ]; then
  # start aerolyzer virtual env
  source $INST_DIR/.virtualenvs/aerolyzer/bin/activate

  # update Aerolyzer
  cd $APP/Aerolyzer
  python manage.py migrate

  echo "Running Aerolyzer App at http://127.0.0.1:8000/app"
  
  # start Aerolyzer
  python manage.py runserver
fi

if [ $mode = "2" ]; then
  sudo $APP/production/run_production.sh
fi

echo "We out fam!"
