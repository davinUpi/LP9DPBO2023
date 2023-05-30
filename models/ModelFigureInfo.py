from Config import Config
from models.Database import Database
from objects.FigureCard import FigureCard

class ModelFigureInfo(Database):
    
    def __init__(self, host=Config.dbhost, user=Config.dbuser, password=Config.dbpass, dbname=Config.dbname) -> None:
        super().__init__(host, user, password, dbname)
    
    def getAll(self):
        query = 'SELECT * FROM figure_info'
        self._execute(query)
        result = self._cursor.fetchall()
        self._cursor.close()
        figureCards = []
        for row in result:
            figureCards.append(
                FigureCard(
                    id=row[0],
                    name=row[1],
                    img = row[2],
                    type = row[3],
                    manufacturer = row[4],
                    series = row[5],
                )
            )
        
        return figureCards
    
    def getById(self, id):
        query = f"SELECT * FROM figure_info WHERE id = {id}"
        self._execute(query)
        result = self._cursor.fetchone()
        return FigureCard(
                    id=result[0],
                    name=result[1],
                    img = result[2],
                    type = result[3],
                    manufacturer = result[4],
                    series = result[5],
                )