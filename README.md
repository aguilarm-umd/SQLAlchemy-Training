The sqlite database is in-memory which made things easy, but the postgres database could not be done in-memory. I decided to then setup a postgres database using Docker.

**A few prerequisites:**
*After installing postgres, create a super user named postgres:*
> createuser -s postgres

*~~Also note your ip address to change the ip address in conn_url in the toy.py file.~~*
* ~~When I was trying to connect to the database I thought it would work with localhost, but I had to use my ip address instead.~~

**The steps are as follows in a terminal (I use zsh if that has any effect):**

> docker run -d -p 5432:5432 --name postgres-test -e POSTGRES_PASSWORD=password postgres

> docker exec -it postgres-test bash

> psql -U postgres

> CREATE DATABASE testdb;

~~Now in the toy.py file change conn_url so that instead of 10.204.153.107 it's your ip address.~~

**Summary of Steps**

* Created a docker container named postgres-test with password "password" that was ported to 5432
* Went into container
* Logged in as user "postgres" and created a database named "testdb"
* ~~Changed the ip address in toy.py to match user's address~~