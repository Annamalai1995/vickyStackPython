#class and object with class & instance attribute
class a:
    name="raja"     #class attri
    def __init__(self,ss1):    #INStance attr
        self.ss1=ss1
        
obj1=a("sam")
obj2=a("GOg")
print("play is boy{}".format(obj1.__class__.name));
print("gOD is boy{}".format(obj2.__class__.name));
print("car is {}".format(obj1.ss1))
print("name is {}".format(obj2.ss1))
#class and object methods
class car:
    #cname="BENZ"
    def  __init__(self,name):
        self.name = name
    def LUxary(self):
        print("Its a costly car for {}".format(self.name))
c=car("BMW");
c1=car("SS");
c.LUxary()
c1.LUxary()
        