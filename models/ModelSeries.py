from Config import Config
from models.Database import Database
from objects.Series import Series

class ModelSeries(Database):
    
    def __init__(self, host=Config.dbhost, user=Config.dbuser, password=Config.dbpass, dbname=Config.dbname) -> None:
        super().__init__(host, user, password, dbname)
    
    def getAll(self):
        query = 'SELECT * FROM series'
        self._execute(query)
        result = self._cursor.fetchall()
        self._cursor.close()
        series = []
        for row in result:
            series.append(Series(id=row[0], name=row[1], nFigures=row[2]))
        
        return series
    
    def getById(self, id):
        query = f"SELECT * FROM series WHERE series_id = {id}"
        self._execute(query)
        row = self._cursor.fetchone()

        return Series(id=row[0], name=row[1], nFigures=row[2])
        