from Item import Item

class ContinusItem(Item):
    def __init__(self,count,name):
        super().__init__(name)
        self.count=count

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        if isinstance(value, int):
            self.__count = float(value)
        else:
            raise TypeError("value must be int data type.")
     # casting
    def __str__(self):
        return '{} {}'.format(self.name,self.count)
  
    # representation of an object
    def __repr__(self):
        return '({}, {})'.format(self.name, self.count)