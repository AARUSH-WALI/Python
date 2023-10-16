my_dict={"name":"John","age":20,"city":"Udhampur"}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print("printing keys......")
for k in my_dict:
    print(k)
print('printing values......')
for v in my_dict.values():
    print(v)
print("difference in printing keys between for loop and built in function")
print("*****using for loop*****")
for k in my_dict:
    print(k)
print("*****built in*****")
print(my_dict.keys())

for k,v in enumerate(my_dict.items)
