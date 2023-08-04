def hello():
    print("hello im sasi")
hello()
def mani(name,age):
    
    print(name,age)
mani("sasi",23)
'''def sugan():
    tamil=int(input("enter your tamil value:"))
    hari=int(input("enter your hari value:"))
    if tamil==hari:
        print("hari and tamil is equal")
    elif tamil<=hari:
        print("hari is gotted big value")
    elif tamil>=hari:
        print("tamil is gotted big value")

    else:
        print("non of these")
sugan()'''
'''def basha():
    for i in range(0,10):
        print(i)
    for x in range(0,100,2):
        print(x)

basha()
'''
#local variable 
#global variable

def annamalai():
    global x,y
    x=20
    y=40
    
annamalai()
print(x+y)
