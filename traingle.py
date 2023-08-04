'''row=3
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end="")
    print('')
'''
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()