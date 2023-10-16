a=[10,20,340]
print("Before append",a)
a.append(32)
print("After append",a)#insert element at end

odd=[1,3,5]
print("odd",odd)
even=[2,4,6]
print("even",even)
odd.extend(even)#use to combine 2 lists
print("after extend",odd)

num=[10,20,30,40]
print("inserting 21 at 1 index using insert(1,21)")
num.insert(1,21)
print(num)

language=["Python","Swift","C++"]
language[2]='C'
print(language)
