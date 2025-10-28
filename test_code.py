import os, sys # E401: multiple imports on one line

def my_function(  arg1,arg2): # E271: multiple spaces after keyword
   # E303: too many blank lines (3)
   
   
   x=arg1+arg2 # E225: missing whitespace around operator
   print("result is",x) # E231: missing whitespace after ','
   if x>10: # E272: multiple spaces before keyword
    print('greater')
   return x

class myclass: # E302: expected 2 blank lines, found 0
               # N801: class name 'myclass' should use CapWords
    def __init__(self, value):
        self.VeryLongVariableName = value # N803: argument name 'value' should be lowercase
                                        # N815: variable 'VeryLongVariableName' in class scope should be lowercase

    def another_method(self):
        print(self.VeryLongVariableName)

# E501: line too long (over 79 characters)
this_is_a_very_very_very_very_very_very_very_very_very_very_very_long_line_of_code = "hello"

# F841: local variable 'unused_var' is assigned to but never used
unused_var = 1

# E305: expected 2 blank lines after class or function definition
print("done")