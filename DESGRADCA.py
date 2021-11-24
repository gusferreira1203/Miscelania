# This is able to tell the user what the type of an object is
string_example = "string"
int_example = 1
float_example = 1.1
type_of_string = type(string_example)
# <class 'str'>
type_of_int = type(int_example)
# <class 'int'>
type_of_float = type(float_example)
# <class 'float'>
print(int_example.isnum(), float_example.isnum(), string_example.isnum())
