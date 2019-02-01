from CountType import CountType


class Category:
    
    def __init__(self,name,parent,id,type):
      self.name=name
      self.parent=parent
      self.id=id
      self.type=type


    @property
    def type(self):
      return self.__type
    
    @type.setter
    def type(self, value):
      self.__type=value

    @property
    def id(self):
      return self.__id
    
    @id.setter
    def id(self, value):
      self.__id=value

    @property
    def name(self):
      return self.__name
    
    @name.setter
    def name(self, value):
      self.__name=value

    @property
    def parent(self):
      if self.__parent is None:
          return Category("",None,-1,CountType.NONE)
      return self.__parent
    
    @parent.setter
    def parent(self, value):
      self.__parent=value
    
     # casting
    def __str__(self):
        str=self.name
        if self.parent.id!=-1:
            str=str+" in zirmajmoe {}".format(self.parent.name)
        str=str+" type is {}".format(self.type)
        return str
  
    # representation of an object
    def __repr__(self):
        str=self.name
        if self.parent.id!=-1:
            str=str+" in zirmajmoe {}".format(self.parent.name)
        str=str+" type is {}".format(self.type)
        return str
   
    
    