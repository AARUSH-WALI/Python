list1=[True, True, True]
list2=[True, False, True]
print(all(list1))
print(all(list2))
list3=[False, False, False]
list4=[True, True, True]
print(any(list3))
print(any(list4))
print(ascii("Kot, \nBhalwal!"))
print(ord("a"))
print(ord(" "))
print(ord(","))
print(ord("*"))

print(bin(10))#convrts an integer to an binary string
print(bin(15))
print(bool(0))#converts a value to boolean(true or false)
print(bool(42))
print(bool([]))
print(bool([1,2]))
byte_array=bytearray([65,66,67])#returns a mutable byte array object from an iterable nof integers
print(byte_array)
byte_array[0]=88
print(byte_array)

byte_string=bytes([68,69,70])#returns an immutable bytes object from an iterable of integers.
print(byte_string)


def my_function():
    return 42
print(callable(my_function))#returns True if the object appears callable (can be called as a function), otherwise false.
print(callable(42))
