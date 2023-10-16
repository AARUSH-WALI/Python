my_list=[1,2,3,4,5,6]

def change_value(my_list):
    my_list[3]=30
    print("value inside the list:",my_list)
    print("Address is:",id(my_list))#print the memory address of my_list
    return
print("Before function call,my_list:",my_list)
print("Address:",id(my_list))#print the memory address of my_list before function call
change_value(my_list)
print("After function call, my_list:",my_list)
print("Address:",id(my_list))#print the memory address of my_list after function call
