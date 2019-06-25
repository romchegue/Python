class MyClass1:
    def __init__(self, name=None, age=0, tel=None, mail=None, job=None):
        self.name = MyClass1.name_converter(self, name)
        self.age = MyClass1.age_checker(self, age)
        self.tel = MyClass1.tel_converter(self, tel)
        self.mail = MyClass1.name_converter(self, mail)[0]
        self.job = job.capitalize()
        MyClass1.self_printer(self)
    def name_converter(self, raw_name):
        if raw_name != None:
            raw_name = raw_name.lower().strip().split()
            proper_name = raw_name.copy()    
            for i in range(len(raw_name)):
                proper_name[i] = raw_name[i].capitalize()
        return(proper_name)
    def age_checker(self, age_value):
        if str(age_value).isdigit() and int(age_value) <= 150:
            return int(age_value)
        else:
            return 0
    def tel_converter(self, raw_number):
        self.tel = ''
        for symbol in str(raw_number):
            if symbol.isdigit():
                self.tel += symbol
        if self.tel[0] in ('7', '8'):
            self.tel = '+7' + self.tel[1:]
        return(self.tel)
    def addattr(self, *attrs):
        self.newattribute = attrs
    def age_changer(self, differ=1):
        self.age += differ
        return(self.age)
    def lastname(self):
        return(self.name.split()[-1])
    def self_printer(self):
        MAX = 0
        for key in self.__dict__.keys():
            if len(key) > MAX:
                MAX = len(key)
        for key in self.__dict__.keys():
            print("{0:<{1}} \t=> {2}".format(key, (MAX - len(key)),self.__dict__[key]))
			
			



