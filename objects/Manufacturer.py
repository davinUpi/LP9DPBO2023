
class Manufacturer:
    def __init__(self, id, name, nFigures) -> None:
        self._id = id
        self._name  = name
        self._nFigures = nFigures
    
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    
    def getNFigures(self):
        return self._nFigures
    
    def setName(self, name):
        self._name = name
    
    '''
        id are primary key, they may not be changed
        directly
    
        n_figures are set by trigger on the db,
        must not be injected!
    '''