from .generation.color import Color

class TerrainType():
    def __init__(self,name,height,colour):
        self.name = name
        self.height = height
        self.colour = colour
    
    def get(self, attrib):
        """
        :param attrib: str
        """
        try:
            return eval("self."+attrib)
        except:
           pass


    