##
# String operations to use with python 
## 

#######################
## Indexing and Slicing 
example_str = "string indexing and slicing"
print(example_str[0])               # => s
print(example_str[2:5])             # => rin
print(example_str[:5])              # => strin
print(example_str[:-3])             # => string indexing and slic
print(example_str[-7:-3])           # => slic
print(example_str[-7:])             # => slicing
print(example_str.split())          # => ['string', 'indexing', 'and', 'slicing']

###################
## String functions
example_str = "this is a string example "
print(len(example_str))             # => 25
print(example_str.capitalize())     # => This is a string example
print(example_str.upper())          # => THIS IS A STRING EXAMPLE
print(example_str.lower())          # => this is a string example
print(example_str.title())          # => This Is A String Example
# removes extra charachters from 
# the start and end of a string,
# in this case it will remove space 
# from the end of the string
print(example_str.strip(" "))       # => 'this is a string example' 

####################
## Further functions
example_str = "    This is cool\t\n     "
print(example_str.strip())                  # => This is cool
print(example_str.startswith("This"))       # => False
print(example_str.endswith("  "))           # => True
# return the start index of the search 
# keyword if found
print(example_str.find("cool"))             # => 12 
print(example_str.replace("cool", "yep"))   # =>     This is yep
print("cool" in example_str)                # => true