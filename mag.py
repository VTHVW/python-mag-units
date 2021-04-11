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