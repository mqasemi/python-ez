

import jsonpickle as jsonp
import sys, platform, os
from Item import Item
from Items import Items
from ContinusItem import ContinusItem
from DiscritItem import DiscritItem
from Categorey import Category
from CountType import CountType
from Categorys import Categorys
from user import user
from users import users


cats=Categorys()
users=users()
msg=""
current_user=None


def clear_screen():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
            os.system('cls')
    else:
        print('Clear screen is not working.')
    if not current_user is None :
         print("welcom {})".format(current_user.username))
   
       
def show_help():
    if current_user.username=="admin":
        print("1-> insert user")
        print("2-> insert category")
        print("3-> show ctegory")
        print("4-> insert item")
        print("5-> show item")
    else:
        print("1-> list product")
        print("2-> find product")
        print("3-> order item")
        print("4->show statement")
        print("4->remove item from order")


if __name__ == "__main__":

   
    """  us=user("admin","admin","123","admin")
    users.add(us)
    users.save() """
   
    while current_user is None:
        clear_screen() 
        command=input("""
    *****************************************************************************************
    *    weclome to store for use of our service pleas signin with your username or signup  *
    *****************************************************************************************
    1->signin
    2->signup
    3->exit
   {msg} """.format(msg=msg)).lower()
        msg=""
        if command=="1":
            usernam=input("enter username:")
            password=input("enter password:")
            current_user=users.validate_user(usernam,password)
            if current_user is None :
                msg="username or password incorrect!!!!!"
        elif command=="2":
            pass
        elif command=="3":
            break
        else :
            msg=("pleas enter number  from {1,2,3}\n")
    

    while not  current_user is None:
        clear_screen()
        print(msg)
        show_help()
        command=input("select action from menue :")
        msg=""
        if command=="1":
            username=input("enter username:")
            name=input("enter name:")
            lname=input("enter lastname:")
            passw=input("enter password")
            new_user=user(name,lname,passw,username)
            users.add(new_user)
            users.save()
            msg="new user successfuley added"
    




    """ db={}
    c=CountType(1)
    categoris=[]
    behdashti=Category("behdashti",None,1,CountType.NONE)
    ater=Category("ater",behdashti,2,CountType.DESCRIT)

    khoraki=Category("khoraki",None,3,CountType.NONE)
    gosht=Category("gosht",khoraki,4,CountType.CONTINUS)
   
    cats.add(behdashti)
    cats.add(ater)
    cats.add(khoraki)
    cats.add(gosht)

    cats.save()

 """

   
    





    






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










