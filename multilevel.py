class bank:
    def name(self):
        print("Axis bank")
class bank1(bank):
    def name1(self):
        print("hdfc bank")
class bank2(bank1):
    def name2(self):
        print("ICICI bank")
        print("raja")
b=bank2()
b.name()
b.name1()
b.name2()