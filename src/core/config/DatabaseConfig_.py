class DatabaseConfig:

    def __init__(self):
        self.DB_USERNAME = '<DATABASE_USERNAME>'
        self.DB_PASSWORD = '<DATABASE_PASSWORD>'
        self.DB_HOST = 'localhost'
        self.DB_PORT = 3306
        self.DB_NAME = '<DATABASE_NAME>'

    def get_connection(self):
        return f'mysql+mysqlconnector://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?use_pure=True'
