first = "John"
last = "Smith"

message = first + " ["+ last + "] is a coder." # Harder to read

msg = f"{first} [{last}] is a coder" # "f" string is used to dynamically insert values into strings
print(msg)

name = "waqas"
age = 17

message = "My name is " + name + "and i am " + str(age) + " years old."

msg = f"My name is {name} and i am {age} years old." # Easier to read
print(msg)