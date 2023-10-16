#formatted string
s=str(input("enter your string\n"))
a=0
b=len(s)-1
flag=1
while a<b:
    if(s[a]!=s[b]):
        flag=0
        break
    else:
        a=a+1
        b=b-1
print(bool(flag))
