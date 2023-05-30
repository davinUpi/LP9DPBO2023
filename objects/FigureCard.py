
class FigureCard:
    def __init__(self, id, name, img, type, manufacturer, series) -> None:
        self._id = id
        self._name = name
        self._img = img
        self._type =type
        self._manufacturer = manufacturer
        self._series = series
    
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getImg(self):
        return self._img
    
    def getType(self):
        return self._type
    
    def getManufacturer(self):
        return self._manufacturer
    
    def getSeries(self):
        return self._series
        
    '''
        id is primary key and autoincremented, must
        not be set manually
        
        No setter as this object is to fetch values
        from a View Table
    '''