'''

#list
# index always starts with 0,1,2,3,......
'''
balance=[200000,19000,3400,10999]

def debit(money=0,pos=0):
    if money<=balance[pos]:
        balance[pos]-=money
        print(money, "debited")
        return balance[pos]
    else:print("Can't debit")

hai=debit(8000,3)
print(hai)

 
def simple(single=0):
    single*single

yet=simple(12)
print(yet)

#no parameter with return
def demo():
    exp=int (input("Tell us experience: "))
    skill=input("Tell us skill: ")
    if exp>=4 and exp<6 and skill == 'python' or skill=='java':
         return "Promoted as Team Lead"
    elif exp>=6 and exp<10 and skill == 'agile' or skill == 'devops':
        return "Promoted as Project Manager"
    return "Be as associate"

desig=demo()
print(desig)