from Categorey import Category
from CountType import CountType
import jsonpickle as jsonp
class Categorys:


    def get_category(self,id):
        categorys=self.list_categorys()
        for cat in categorys:
            if cat.id==id:
                return cat
        return None

    def list_categorys(self):
        with open('db/categorys.json',"r") as db:
            records=db.read()
            if(records!=None and len(records)>0):
                return(jsonp.decode(records))
        return []

    def __init__(self):
        self.__categorys=self.list_categorys()
        
                
        

    def add(self, item):
        if isinstance(item,Category ):
            self.__categorys.append(item)
        else:
            raise TypeError("value must be cateogry class.")

    def show(self):
        return self.__categorys

    def __iter__(self):
        yield from self.__categorys
    
    def __contains__(self, item):
        for i in self:
            if item.id == i.id:
                return True
        return False

    def __add__(self, other):
        self.add(other)
        return self
    
    def __len__(self):
        return len(self.__categorys)

    def __str__(self):
        return str(self.__categorys)

    
                   
              
    
    def save(self):
        with open('db/categorys.json',"w") as db:
            db.write(jsonp.encode(self.__categorys))