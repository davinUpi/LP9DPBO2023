from Config import Config
from models.Database import Database
from models.ModelFigureType import ModelFigureType
from models.ModelManufacturer import ModelManufacturer
from objects.Figure import Figure

class ModelFigure(Database):
    
    def __init__(self, host=Config.dbhost, user=Config.dbuser, password=Config.dbpass, dbname=Config.dbname) -> None:
        super().__init__(host, user, password, dbname)
    
    def getAll(self):
        query = 'SELECT * FROM figures'
        result = self._execute(query)
        modelType = ModelFigureType(
            host=self._host,
            password=self._password,
            dbname=self._dbname,
            user=self._user
        )
        modelMan = ModelManufacturer(
            host=self._host,
            password=self._password,
            dbname=self._dbname,
            user=self._user
        )
        
        figures = []
        for row in result:
            figures.append(Figure(id=row[0], name=row[1], img=row[2], type=modelType.getById(row[3]), manufacturer=modelMan.getById(row[4])))
        
        return figures
    
    def getById(self, id):
        query = f"SELECT * FROM manufacturers WHERE man_id = {id}"
        result = self._execute(query)
        
        modelType = ModelFigureType(
            host=self._host,
            password=self._password,
            dbname=self._dbname,
            user=self._user
        )
        modelMan = ModelManufacturer(
            host=self._host,
            password=self._password,
            dbname=self._dbname,
            user=self._user
        )
        
        if result is not None and len(result) > 0:
            row = result[0]
            return Figure(id=row[0], name=row[1], img=row[2], type=modelType.getById(row[3]), manufacturer=modelMan.getById(row[4]))
        else:
            return None