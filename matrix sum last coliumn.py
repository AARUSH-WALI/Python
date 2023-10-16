list=[[1,2,3,4],#-------0
      [5,6,7,8],#-------1
      [9,10,11,12],#----2
      [13,14,15,16]]#---3
length=len(list)
sum=0
for r in list:
    for c in range(length):
        if c==3:
            sum+=r[c]
    
print("Sum of last column=",sum)
#another method
'''for r in list:
a+=r[3]
print(a)'''
