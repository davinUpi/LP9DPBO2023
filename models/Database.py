from abc import ABC
from Config import Config
import mysql.connector

class Database(ABC):
    def __init__(
        self, 
        host = Config.dbhost, 
        user = Config.dbuser, 
        password = Config.dbpass, 
        dbname = Config.dbname
        ) -> None:
        self._host = host
        self._user = user
        self._password = password
        self._dbname = dbname
        self._mysqli = mysql.connector.connect(
            host = self._host,
            user = self._user,
            password = self._password,
            database = self._dbname
        )
        self._cursor = self._mysqli.cursor()
    
    def _execute(self, query):
        try:
            self._cursor.execute(query)
            self._mysqli.commit()
            
        except mysql.connector.Error as e:
            print(f"Error: {e}")
    
    def close(self):
        self._cursor.close()
        self._mysqli.close()