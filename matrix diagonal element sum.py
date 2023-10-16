list=[[1,2,3,4],#-------0
      [5,6,7,8],#-------1
      [9,10,11,12],#----2
      [13,14,15,16]]#---3
length=len(list)
sum=0
for r in range(0,len(list)):
    for c in range(0,len(list[r])):
        if r==c:
            sum+=list[r][c]
    
print("Sum of diagonal element=",sum)
