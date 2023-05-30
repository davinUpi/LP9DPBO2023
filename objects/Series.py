
class Series:
    
    def __init__(self, id, name, nFigures) -> None:
        self._id = id
        self._name = name
        self._nFigures = nFigures
    
    def setId(self, id):
        self._id = id
    
    def setName(self, name):
        self._name = name
    
    def setNFigures(self, nFigures):
        self._nFigures = nFigures
    
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getNFigures(self):
        return self._nFigures