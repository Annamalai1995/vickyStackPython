class college:
     def name(self):
         print("college is good ")
  
class clgname(college):
     def name1(self):
         print("KSR college  ")
  
class clgloctaion(college):
     def name2(self):
         print("Thiruchengode")
  
class placement(clgname,clgloctaion,college):
     def name3(self):
         print("Good")
  

p = placement()
p.name1()
p.name()
p.name3()
p.name2()