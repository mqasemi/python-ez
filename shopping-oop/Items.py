import Item

class Items:
    def __init__(self):
        self.__items = list()
    
    def add(self, item):
        if isinstance(item, Item):
            self.__items.append(item)
        else:
            raise TypeError("value must be Item class.")

    def show(self):
        return self.__items

    def __iter__(self):
        yield from self.__items
    
    def __contains__(self, item):
        for i in self:
            if item.name == i.name and item.count == i.count:
                return True
        return False

    def __add__(self, other):
        self.add(other)
        return self
    
    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)
    
