from enum import Enum,IntFlag
class CountType( Enum):
    DESCRIT=0
    CONTINUS=1
    NONE=2
    def default(self,o):
        return o.__dict__

    def __str__(self):
        str=""
        if self.value==0:
            str="descrit"
        elif self.value==1:
            str="continu"
        else:
            str="any"
       
        return str
    def to_json(self):
        return '{},{}'.format(self.value,self.name)
    def decode(self,json):
        name_value=json.split(',')
        self.name=name_value[1]
        self.value=name_value[0]




  