import jsonpickle as jsonp
from user import user

class users:
    
    def __init__(self):
        self.__users=self.list_users()
    
    def list_users(self):
        with open('db/users.json',"r") as db:
            records=db.read()
            if(records!=None and len(records)>0):
                return(jsonp.decode(records))
        return []
    def get_user(self,username):
        users=self.list_users()
        for user in users:
            if user.username==username:
                return user
        return None
    def add(self, item):
        if isinstance(item,user ):
            self.__users.append(item)
        else:
            raise TypeError("value must be user class.")
    def __iter__(self):
        yield from self.__users
    
    def __contains__(self, item):
        for i in self:
            if item.username == i.username:
                return True
        return False
    
    def save(self):
        with open('db/users.json',"w") as db:
            db.write(jsonp.encode(self.__users))

    def validate_user(self,username,password=""):
        user=self.get_user(username)
        if  not user  is None and  user.password==password:
            return user
        return None

    