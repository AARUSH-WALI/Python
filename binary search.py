a=[10,23,45,46,47,56,67,90,99,100]
b=int(input("enter the value to search:"))
length=len(a)
mid=len(a)//2
if(b==a[mid-1]):
    print("target value is at index:",mid-1)
elif(b>a[mid])


