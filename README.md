# yummy_recipe_api_v1
A flask-driven restful API for Bucketlist interactions


## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly.
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create virtual environments
* **[PostgreSQL](https://www.postgresql.org/download/)** – Postgres database (https://www.postgresql.org/about/advantages/) over others.
* other dependencies are on requirements.txt.


## Installation / Usage
* If you wish to run your own build, ensure python3 is globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC
    ```
        $ https://github.com/otim22/yummy_recipe_api_v1
    ```


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd yummy_recipe_api_v1
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv -p python3 venv
        $ pip install autoenv
        ```

* #### Install your requirements
    ```
    (venv)$ pip install -r requirements.txt
    ```

* #### Migrations
    On your psql console, create your database:
    ```
    > CREATE DATABASE yummy_recipe_api_db;
    ```
    Then, make and apply your Migrations
    ```
    (venv)$ python manage.py db init

    (venv)$ python manage.py db migrate
    ```

    And finally, migrate your migrations to persist on the DB
    ```
    (venv)$ python manage.py db upgrade
    ```

* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ flask run
    ```
    You can now access the app on your local browser by using
    ```
    http://localhost:5000/recipes/
    ```
