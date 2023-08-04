a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
#print(a)
#key names
for i in a:
    print(i)
#values
for i in a:
    print(a[i])
#using values 
for i in a.values():
    print(i)
#using keys 
for i in a.keys():
    print(i)
#using items
for i,j in a.items():
    print(i,j)
