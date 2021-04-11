
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

class Mag(object):
    def __init__(self,names:list, abrvs:list,values:list,delta_unit:int=None,delta_unit_top:int=None,delta_unit_bottom:int=None):
        if len(names) == len(abrvs) == len(values) and type(names) == type(abrvs) == type(values) == list:                
            if delta_unit:
                self.top = self.bottom = delta_unit
            else:
                if delta_unit_top:
                    self.top=delta_unit_top
                else:
                    self.top=1
                if delta_unit_bottom:
                    self.bottom=delta_unit_bottom
                else:
                    self.bottom=1
            index=0
            self.mag_list:dict=dict()
            for value in values:
                self.mag_list[value]={"full_name":names[index],"abrv":abrvs[index]}
                index+=1
        else:
            raise TypeError("The arguments have to be same sized lists")
        self.mag_list=dict(sorted(self.mag_list.items(), key=lambda item: item[0],reverse=True))
    
    def parse_value(self,value:int,full:bool=False):
        max=list(self.mag_list.keys())[0]
        min=list(self.mag_list.keys())[-1:][0]
        if value >= max:
            if full:
                return (round(value/max,ndigits=13),self.mag_list[max]["full_name"])
            return (round(value/max,ndigits=13),self.mag_list[max]["abrv"])
        if value <= min:
            if full:
                return (round(value/min,ndigits=13),self.mag_list[min]["full_name"])
            return (round(value/min,ndigits=13),self.mag_list[min]["abrv"])
        for mag, names in self.mag_list.items():
            test=value/mag
            if mag >= self.top:
                if self.top > test >= 1:
                    if full:
                        return (round(test,ndigits=13),names["full_name"])
                    return (round(test,ndigits=13),names["abrv"])
            elif mag <= self.bottom:
                if self.bottom > test >= 1:
                    if full:
                        return (round(test,ndigits=13),names["full_name"])
                    return (round(test,ndigits=13),names["abrv"])
        return (value,"")


mag1000=Mag(
    [
        "Yotta",
        "Zetta",
        "Exa",
        "Peta",
        "Tera",
        "Giga",
        "Mega",
        "Kilo",
        "milli",
        "micro",
        "nano",
        "pico",
        "femto",
        "atto",
        "zepto",
        "yocto"
    ],
    [
        "Y",
        "Z",
        "E",
        "P",
        "T",
        "G",
        "M",
        "K",
        "m",
        "μ",
        "n",
        "p",
        "f",
        "a",
        "z",
        "y"
    ],
    [
        10**24,
        10**21,
        10**18,
        10**15,
        10**12,
        10**9,
        10**6,
        10**3,
        10**-3,
        10**-6,
        10**-9,
        10**-12,
        10**-15,
        10**-18,
        10**-21,
        10**-24
    ],
    delta_unit=1000
)

mag1024=Mag(
    [
        "Yobi",
        "Zebi",
        "Exbi",
        "Pebi",
        "Tebi",
        "Gibi",
        "Mebi",
        "Kibi",
    ],
    [
        "Yi",
        "Zi",
        "Ei",
        "Pi",
        "Ti",
        "Gi",
        "Mi",
        "Ki"
    ],
    [
        1024**8,
        1024**7,
        1024**6,
        1024**5,
        1024**4,
        1024**3,
        1024**2,
        1024
    ],
    delta_unit_top=1024
)

class Value():
    def __init__(self,value : int, unit : Unit, magnitude:Mag=None):
        
        pass
