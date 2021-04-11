class Unit(object):
    def __init__(self,name:list,abrv:list):
        if type(name) == list or type(name) == str and type(abrv) == str:
            if type(name) == list and 1 < len(name) <=2:
                Exception("If name is a list it must contain from 1 to 2 elements")
            self.name = name
            self.abrv = abrv
        else:
            raise TypeError("name must be a list oa a string and abrv must be a string")
    
    def full_name(self):
        if type(self.name) == str:
            return self.name
        else:
            return self.name[0]

    def plural_name(self):
        if type(self.name) == str:
            return self.name
        else:
            if len(self.name) >= 2:
                return self.name[1]
            else:
                return self.name[0]


class ComplexUnit(object):
    def __init__(self,num:dict=None,denom:dict=None,name:list=None,abrv:list=None):
        if num  is None and denom is None:
            raise TypeError("Must containt at least one denominator or numerator")
        self.numerator=dict()
        self.denominator=dict()
        for key,value in num:
            if type(key) == ComplexUnit:
                self *= key
            else:
                if key in self.numerator.keys():
                    self.numerator[key]+=value
                elif key in self.denominator.keys():
                    self.denominator[key]-=value
                    if self.denominator[key] == 0:
                        del self.denominator[key]
                else:
                    self.numerator[key]=value
        for key,value in denom:
            if type(key) == ComplexUnit:
                self /= key
            else:
                if key in self.numerator.keys():
                    self.numerator[key]-=value
                    if self.numerator[key] == 0:
                        del self.numerator[key]
                elif key in self.denominator.keys():
                    self.denominator[key]+=value
                else:
                    self.denominator[key]=value
        if name and abrv:
            self.unit=Unit(name,abrv)
        else:
            self.unit=None
        
    def __mul__(self,units):
        if type(units) == Unit:
            if units in self.numerator.keys():
                self.numerator[units]+=1
            elif units in self.denominator.keys():
                self.denominator[units]-=1
                if self.denominator[units] == 0:
                    del self.denominator[units]
            else:
                self.numerator[units]=1
        elif type(units) == ComplexUnit:
            for unit,value in units.numerator.items():
                for _ in range(0,value):
                    self*=unit
            for unit,value in units.denominator.items():
                for _ in range(0,value):
                    self/=unit
        else:
            TypeError("Only Unit and ComplexUnit supported for this operation")
                
    def __truediv__(self,units):
        if type(units) == Unit:
            if units in self.numerator.keys():
                self.numerator[units]-=1
                if self.numerator[units] == 0:
                    del self.numerator[units]
            elif units in self.denominator.keys():
                self.denominator[units]+=1
            else:
                self.denominator[units]=1
        elif type(units) == ComplexUnit:
            for unit,value in units.numerator.items():
                for _ in range(0,value):
                    self/=unit
            for unit,value in units.denominator.items():
                for _ in range(0,value):
                    self*=unit
        else:
            TypeError("Only Unit and ComplexUnit supported for this operation")

    def __imul__(self,units):
        self=self*units
                
    def __idiv__(self,units):
        self=self/units

    def short_name(self):
        if self.unit:
            return self.unit.abrv

    def full_name(self):
        if self.unit:
            return self.unit.full_name()

    def plural_name(self):
        if self.unit:
            return self.unit.plural_name()
    
    def long_name(self):
        ret=""
        if len(self.numerator) > 0:
            for key,value in self.numerator.items():
                if value <=1:
                    ret+="⋅"+key.abrv
                else:
                    ret+="⋅"+key.abrv+[self.__num_to_supertext(int(i)) for i in str(value)].join('')
        else:
            if len(self.denominator) > 0:
                ret+="11"
        ret+="/"
        if len(self.denominator) > 0:
            for key,value in self.denominator.items():
                if value <=1:
                    ret+=key.abrv+"⋅"
                else:
                    ret+=key.abrv+[self.__num_to_supertext(int(i)) for i in str(value)].join('')+"⋅"
        return ret[1:-1]

    def __num_to_supertext(self,int):
        if int == 0:
            return '⁰'
        elif int == 1:
            return '¹'
        elif int == 2:
            return '²'
        elif int == 3:
            return '³'
        elif int == 4:
            return '⁴'
        elif int == 5:
            return '⁵'
        elif int == 6:
            return '⁶'
        elif int == 7:
            return '⁷'
        elif int == 8:
            return '⁸'
        elif int == 9:
            return '⁹'