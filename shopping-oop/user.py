class user:
    def __init__(self,name,lastname,password,username):
        self.name=name
        self.lastname=lastname
        self.password=password
        self.username=username
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,value):
        self.__username=value
    
    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self,value):
        self.__lastname=value

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):
        self.__password=value
    
    def __str__(self):
        return "name:{name}\n lastname:{lastname}\n".format(name=self.name,lastname=self.lastname)