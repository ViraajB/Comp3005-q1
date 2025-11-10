Install python dependency-

pip install psycopg2-binary

open terminal and run

psql -U postgres -c "CREATE DATABASE school;"

from root run

psql -U postgres -d school -f db/schema.sql

default password is "postgres"

run the application

python app/main.py

Youtube Video

https://youtu.be/jEjjfNTRIyE

