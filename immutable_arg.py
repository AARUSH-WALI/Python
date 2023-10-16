a=10

def change_value(a):
    a=20
    print("Inside Function, address:",id(a))
    return a

print("Before function call, a=",a,"address:",id(a))

a=change_value(a)

print("After function csll,a=",a,"address:",id(a))
