'''#demonstration of LIST
prop=["Annamalai",5.5,70,'M']
print(prop)
#adding the new elements in end if list
prop.append('Software developer')
print(len(prop))
print(prop)
#adding new elements in list
prop.insert(4,15.5)
print(prop)
#replace the data in respective position
prop[5]='Team lead'
print(prop)'''
#adding values in list
monthly=[7000,8000,13000,3000,25000]
print(min(monthly))
#sum of the list
print(sum(monthly))
#remove and pop the list operation
monthly.remove(3000)
print(monthly)
print(monthly.pop())
print(monthly.pop(1))
print(monthly)
print(monthly.reverse())
print(monthly)

