tup = (1,88,22,99,66,44,5,8,254,8)
val = int(input("enter the number you want to search:"))
idx = 0
for el in tup:       #linear search
        if(el == val):
            print("found at index :",idx)
        idx +=1
