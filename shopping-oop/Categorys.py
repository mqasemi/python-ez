from Categorey import Category
from CountType import CountType
class Categorys:


    def get_category(self,id):
        with open('categorys.csv',"r") as db:
            records=db.readlines()
            for record in records :
                if (record.split(','))[2]==id:
                    return record.split(',')
        return []

    def __init__(self):
        self.__categorys=[]
        with open('categorys.csv',"r") as db:
                records=db.readlines()
                for record in records :
                    
                   # parent=Category()
                    record_property=record.split(',')
                    if record_property[1]!="-1":
                        parent_property=self.get_category(record.split(',')[1])
                        parent=Category(parent_property[0],None,parent_property[2],CountType(int(record_property[3])))
                    else:
                        parent=None

                    category=Category(record_property[0],parent,record_property[2],CountType(int(record_property[3])))
                    self.__categorys.append(category)


                
        

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
        with open('categorys.csv',"w") as db:
            for i in self:
                record="{},{},{},{},{}".format(i.name,i.parent.id,i.id,i.type.value,"\n")
                db.write(record)