'''bio={"Name":"Annamalai","Age":25,"Native":"salem"}
print(bio)
#clearMEthod
bio.clear()
print(bio)
print(bio)
#copyMEthod
bio={"Name":"Annamalai","Age":25,"Native":"salem"}
a=bio.copy()
print(a)
#get method
a=bio.get("Native")
print(a)
a=bio.get("car", "Altroz")
print(a)
#items method
a=bio.items()
print(a)
#key methid
a=bio.keys()
print(a)
a=bio.keys()
bio["hobby"]="chatting"
print(a)
#pop
bio.pop("Age")
print(bio)
a=bio.pop("Name")
print(a)'''
#popitems
bio={"Name":"Annamalai","Age":25,"Native":"salem"}
print(bio)
bio.popitem()
print(bio)
#set default
a=bio.setdefault("frnds","pp")
print(a)
#update
bio.update({"car":"altroz"})
print(bio)
#values
a=bio.values()
print(a)
a=bio.values()
bio["CRH"]="pk"
print(a)