class DatabaseConfig:

    def __init__(self):
        self.DB_USERNAME = 'root'
        self.DB_PASSWORD = 'Maverick782'
        self.DB_HOST = 'localhost'
        self.DB_PORT = 3306
        self.DB_NAME = 'my_flask_project'

    def get_connection(self):
        return f'mysql+mysqlconnector://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?use_pure=True'
