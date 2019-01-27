
class Item:
    # attribute

    #constructor
    def __init__(self, name):
        self.name = name
       
    
    # properties
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if value.isalpha():
                self.__name = value
            else:
                raise ValueError("value must be alphabet.")
        else:
            raise TypeError("value must be str data type.")


    # method
    # 
    # magic method    
    def __add__(self, other):
        total = self.__count + other
        self.__count = total
        return total
    
    def __iadd__(self, other):
        if isinstance(other, int):
            self.__count = self.__count + other
            return self
        else:
            raise TypeError("other must be int data type.")

    # casting
    def __str__(self):
        return '{} '.format(self.__name)
  
    # representation of an object
    def __repr__(self):
        return '({})'.format(self.__name)