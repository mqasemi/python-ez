from enum import Enum
class CountType(Enum):
    DESCRIT=0
    CONTINUS=1
    NONE=2
    def __str__(self):
        str=""
        if self.value==0:
            str="descrit"
        elif self.value==1:
            str="continu"
        else:
            str="any"
       
        return str
  