import re

string = '  Hello  World   From Pankaj \t\n\r\tHi There  '

print('Remove all spaces using RegEx:\n', re.sub(r"\s+", "", string), sep='')  # \s matches all white spaces
print()

print('Remove leading spaces using RegEx:\n', re.sub(r"^\s+", "", string), sep='')  # ^ matches start
print()

print('Remove trailing spaces using RegEx:\n', re.sub(r"\s+$", "", string), sep='')  # $ matches end
print()

print('Remove leading and trailing spaces using RegEx:\n', re.sub(r"^\s+|\s+$", "", string), sep='')  # | for OR condition
