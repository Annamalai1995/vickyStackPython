class bank:
    def __init__(self):
        self.__value=20  #private variable
    
    def __sam(self):
       # print("value:",self.__value)
        
        print("Name sam")
        print("A/c 14522186")
        print("Amt:20000")
        print("place:salem")
        print("\n")
    def __priya(self):
        #self.__sam()
        print("Name priya")
        print("A/c 145452186")
        print("Amt:200000")
        print("place:salem")
b=bank()
b._bank__sam()
b._bank__priya()
#b._bank__value()
print("value:",b._bank__value)
#b.__value()
#b.sam()
#b.priya()
