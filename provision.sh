source /tmp/.venv/register-metadata/bin/activate

cd /vagrant/apps/register-metadata

#Create/update the tables in postgres
python manage.py db upgrade
