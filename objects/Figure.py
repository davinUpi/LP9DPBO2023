
class Figure:
    def __init__(self, id, name, img, type, manufacturer) -> None:
        self._id = id
        self._name  = name
        self._img  = img
        self._type = type
        self._manufacturer = manufacturer
    
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
    
    def setName(self, name):
        self._name = name
    
    def setImg(self, img):
        self._img = img
    
    def setType(self, type):
        self._type = type
    
    def setManufacturer(self, manufacturer):
        self._manufacturer = manufacturer
        
    '''
        id is primary key and autoincremented, must
        not be set manually
    '''