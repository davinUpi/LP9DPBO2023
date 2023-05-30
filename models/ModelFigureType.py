from Config import Config
from models.Database import Database
from objects.FigureType import FigureType

class ModelFigureType(Database):
    
    def __init__(self, host=Config.dbhost, user=Config.dbuser, password=Config.dbpass, dbname=Config.dbname) -> None:
        super().__init__(host, user, password, dbname)
    
    def getAll(self):
        query = 'SELECT * FROM figure_types'
        self._execute(query)
        result = self._cursor.fetchall()
        self._cursor.close()
        types = []
        for row in result:
            types.append(FigureType(id=row[0], name=row[1], nFigures=row[2]))
        
        return types
    
    def getById(self, id):
        query = f"SELECT * FROM figure_type WHERE ftype_id = {id}"
        self._execute(query)
        row = self._cursor.fetchone()
        return FigureType(id=row[0], name=row[1], nFigures=row[2])
