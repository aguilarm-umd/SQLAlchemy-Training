The sqlite database is in-memory which made things easy, but the postgres database could not be done in-memory. I decided to then setup a postgres database using Docker.

**A few prerequisites after cloning:**
*Install the Postgres App from here: https://postgresapp.com/*
* Don't Initialize a new server
* Also run this command:
> sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp

*Install pyenv*
> brew install pyenv

*In the repo create a python 3.7.13 virtual environment*
> pyenv virtualenv 3.7.13 SQLAlchemy-Training

*Install the dependencies for the project in the repo (In ZSH I had to put single quotes)*
> pip install -e '.[dev]'

**The steps are as follows:**

> docker build -t test-image ./

> docker run -d -p 5432:5432 --name postgres-test test-image

> ./toy.py

**Summary of Steps**

* Built Docker image for the Postgres Server using the Dockerfile in the repo
* Created a container for the image that is ported to localhost:5432
* Ran the toy.py file as an executable.