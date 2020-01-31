# Flask Custom Base Project
![build-status](https://travis-ci.org/piinalpin/flask-custom-base-project.svg?branch=master)

Create base project or frame for new project Flask with Authorization User

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## How to use ?
1. Install the requirements library `pip install -r requirements.txt`
2. Migrate the database, this project using MySQL Database. `flask db init && flask db migrate`
3. Edit first migration file, add following codes then call `seed_data()` into `def upgrade():`
    ```Python
    from datetime import datetime
    def seed_data():
        app_user = sa.sql.table('app_user',
                                sa.Column('id', sa.Integer()),
                                sa.Column('created_at', sa.TIMESTAMP()),
                                sa.Column('created_by', sa.Integer()),
                                sa.Column('username', sa.String(length=255)),
                                sa.Column('password', sa.String(length=255)),
                                sa.Column('email', sa.String(length=255)),
                                sa.Column('full_name', sa.String(length=255)),
                                sa.Column('enabled', sa.Boolean()),
                                sa.Column('role', sa.String(length=255)))
        op.bulk_insert(app_user,
                       [
                           {
                               'id': 1,
                               'created_at': datetime.today(),
                               'created_by': 0,
                               'username': '<CHANGE_TO_YOUR_USERNAME>',
                               'password': '<CHANGE_TO_YOUR_HASH_PASSWORD_BASE64>',
                               'email': '<CHANGE_TO_YOUR_EMAIL>',
                               'full_name': '<CHANGE_TO_YOUR_NAME>',
                               'enabled': True,
                               'role': 'SUPERUSER'
                           }
                       ])
    ```
4. Update `core/config/DatabaseConfig.py` with your database.
4. Upgrade your migration into MySQL Database `flask db upgrade`
5. Run the application `python Application.py` for debug or `flask run` for deployment.

## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - The language programming used
* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) - Flask CORS Filter
* [Flask-RestFul](https://flask-restful.readthedocs.io/en/latest/) - Flask RestFul
* [Flask-JWT_Extended](https://flask-jwt-extended.readthedocs.io/en/stable/) - Flask Json Web Token
* [Flask Migrate](https://pypi.org/project/Flask-Migrate/) - The database migration
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - The virtual environment used
* [SQL Alchemy](https://www.sqlalchemy.org/) - The database library
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Flask and SQL Alchemy connector
* [MySQL Connector Python](https://pypi.org/project/mysql-connector-python/) - Connector MySQL for Python
* [MySQL](https://www.mysql.com/) - MySQL Database


## Clone or Download

You can clone or download this project
```
git clone https://github.com/piinalpin/flask-custom-base-project.git
```

## Authors

* **Alvinditya Saputra** - [LinkedIn](https://linkedin.com/in/piinalpin) [Instagram](https://www.instagram.com/piinalpin) [Twitter](https://www.twitter.com/piinalpin)
