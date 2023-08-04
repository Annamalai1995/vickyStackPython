# theatre ticket booking
'''
seat=10;

while seat>0:
    amt=int(input("Enter the amount:"))
    if amt>=120:
        print("You bought",seat," ticket")
        seat-=1
    else:
        print("Insufficent amount to buy ticket")

'''

# theatre ticket booking

seat=30;

while seat>0:
    qty=int(input("Tell us how many tickets you want: "))
    payable=qty*120;
    amt=int(input("Enter the amount:"))
    if amt>=payable:
        print("You bought",qty," ticket")
        seat-=qty
    else:
        print("Insufficent amount to buy ticket payable amount is",payable)

for seat in range(30,0,-1):
    print(seat)

for seat in range(1,31,+2):
    print(seat)