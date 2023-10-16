list=[[1,2,3,4],#-------0
      [5,6,7,8],#-------1
      [9,10,11,12],#----2
      [13,14,15,16]]#---3
sum=0
a=int(input("enter the row to reverse"))
for r in range(0,len(list)):
        if(r==a):
            list.reversed(r)
            print(list[r-1],end=" ")
