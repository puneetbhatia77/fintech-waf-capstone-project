# Fintech App

## Setup PostgreSQL server

psql -U postgres -h localhost -p 5432                   # login to PostgreSQL

CREATE DATABASE fintechdb;                              # create Database

\l                                                      # list databases

exit                                                    # come out of PostgreSQL

psql -U postgres -d fintechdb -h localhost -p 5432      # login to PostgreSQL with given database

### create table

CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    income NUMERIC(10, 2) NOT NULL,
    loan_amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending'
);

-------------------------------------------------------------------------------------------------------

## Run flask app locally
D:\Labs\Capstone projects\fintech_app_db_integration-capstone-project\fintech_app>code .
## run below command from terminal
py api/app.py

#### Running on http://127.0.0.1:5000, notice templates/form.html added to input data.

#### Go to PostgreSQL and check data polupated in table by running below command
SELECT * FROM applications;  

#### Alternate way, comment form.html code and gGo to postman and try to run POST command for http://localhost:5000/register with following JSON code.
{
  "name": "xyz",
  "age": "47",
  "income": "200000",
  "loan_amount": "500000"
}



-----------------------------------------------
## Run flask app using dockerfile

docker build -t fintech_app:V4 .
docker run --env-file .env -p 5000:5000 fintech_app:V4
or
#### To register new user, run docker command with "host.docker.internal" user instead of localhost

docker run -e 'DB_URL="postgresql://username:password@host.docker.internal:5432/fintechdb:V4"' -p 5000:5000 fintech_app:V4








