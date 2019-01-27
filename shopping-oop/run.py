
from Item import Item
from Items import Items
from ContinusItem import ContinusItem
from DiscritItem import DiscritItem
from Categorey import Category
from CountType import CountType



if __name__ == "__main__":
    db={}
    categoris=[]
    behdashti=Category("behdashti",None,1,CountType.NONE)
    ater=Category("ater",behdashti,2,CountType.DESCRIT)

    khoraki=Category("khoraki",None,3,CountType.NONE)
    gosht=Category("gosht",khoraki,4,CountType.CONTINUS)
    

    categoris.append(ater)
    categoris.append(behdashti)
    categoris.append(khoraki)
    categoris.append(gosht)
    db["cat"]=categoris
    





    






"""
print(titem1)
print(titem2)
 items = Items()
item = Item('apple', 2)
item2 = Item('orange', 2)
items.add(item)
items.add(Item('orange', 1))
items.add(Item('bannana', 5))

a = items + item + item2

items.add(Item("kivy", 100))

print(a)

for item in items:
    print(item)

print(len(items))

print(Item('apple', 2) in items) """
# print(item2 in items)










