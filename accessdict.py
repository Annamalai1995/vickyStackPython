a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
print(a["frds"])
b=a["Hobbies"]
print(b)
b=a.get("Hobbies")
print(b)
b=a.keys()
print(b)
a["bike"]="fz"
print(a)
b=a.values()
print(b)
a["car"]="Altroz"
print(b)
b=a.keys()
print(b)