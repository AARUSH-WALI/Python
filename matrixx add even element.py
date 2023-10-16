list=[[1,2,3,4],#-------0
      [5,6,7,8],#-------1
      [9,10,11,12],#----2
      [13,14,15,16]]#-3
sum=0
for r in list:
    for c in r:
        if c%2==0:
            sum+=c
        print(c,end=" ")
    print()
print("Sum of even numbers=",sum)
