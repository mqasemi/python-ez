"""
masood ghasemi

"""


import os
def show_help():
    print('enter "help" to view help ')
    print('enter "show" to view order list')
    print('enter "done" to end order')
    print('enter item name to add to order')
    print('enter "remove" to remove item')


def main():
    show_help()
    orders=[]
    have_order=True
    while have_order:
        command=input('enter an command for help enter "help" :').lower()
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        if command == 'help':
            show_help()
        elif command =='show':
            print(orders)
        elif command =='done':
            have_order=False
        elif command =='remove':
            del_item=input('enter an item to remove: ').lower()
            if del_item in orders :
                orders.remove(del_item)
                print("itme {} deleted !!".format(del_item))
            else:
                print("item {} not exist:".format(del_item))
            
        else :
            if len(command)!=0  :
                if command not in  orders:
                    orders.append(command)
                else : 
                    print("you order this item later")
            else :
                print("you can not enter empty order!!!")
       
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("thank for your order")
    print(orders)
    print("goodby")
                
        


if __name__== "__main__":
  main()
        
