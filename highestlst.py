name=[]
mark=[]
for i in range(5):
    a=input("enter the name")
    b=int(input("Enter the marks"))
    name.append(a)
    mark.append(b)
h=max(mark)
l=min(mark)
print("high mark:",h)
print("low mark:",l)
for i in range(5):
    if h==mark[i]:
        print("Highest mark:",name[i] )
    if l==mark[i]:
        print("Lowest mark: ",name[i])