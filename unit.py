class Unit(object):
    def __init__(self,name:list,abrv:list):
        if type(name) == list:
            if type(abrv) == list:
                if len(abrv) == len(name):
                    self.name = name
                    self.abrv = abrv
                else:
                    raise TypeError("name and abrv must have same lenght")
            else:
                raise TypeError("name and abrv must be the same type")
        else:
            if type(name) == type(abrv) == str:
                self.name = name
                self.abrv = abrv
            else:
                raise TypeError("name and abrv must either be strings or lists")
    
    def full_name(self,index:int=None):
        if index and type(self.name) == str:
            index=None
        if not index:
            return self.name
        else:
            return self.name[index]

    def abrv_name(self,index:int=None):
        if index and type(self.abrv) == str:
            index=None
        if not index:
            return self.abrv
        else:
            return self.abrv[index]
    
    def plural_name(self):
        if type(self.name) == str:
            return self.name
        else:
            if len(self.name) < 2:
                return self.name[0]
            return self.name[1]


class ComplexUnit(object):
    pass