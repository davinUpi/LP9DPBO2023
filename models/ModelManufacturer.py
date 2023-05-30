from Config import Config
from models.Database import Database
from objects.Manufacturer import Manufacturer

class ModelManufacturer(Database):
    
    def __init__(self, host=Config.dbhost, user=Config.dbuser, password=Config.dbpass, dbname=Config.dbname) -> None:
        super().__init__(host, user, password, dbname)
    
    def getAll(self):
        query = 'SELECT * FROM manufacturers'
        self._execute(query)
        result = self._cursor.fetchall()
        self._cursor.close()
        
        manufactures = []
        for row in result:
            manufactures.append(Manufacturer(id=row[0], name=row[1], nFigures=row[2]))
        
        return manufactures
    
    def getById(self, id):
        query = f"SELECT * FROM manufacturers WHERE man_id = {id}"
        self._execute(query)
        row = self._cursor.fetchone()
        return Manufacturer(id=row[0], name=row[1], nFigures=row[2])
        