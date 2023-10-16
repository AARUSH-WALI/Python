list=[[1,2,3,4],#-------0
      [5,6,7,8],#-------1
      [9,10,11,12],#----2
      [13,14,15,16]]#-3
sum=0
for r in range(len(list)):
    for c in list[r]:
        if r==1:
            sum+=c
    
print("Sum of 2nd row=",sum)
