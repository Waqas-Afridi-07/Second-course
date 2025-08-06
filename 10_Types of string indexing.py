# String is a sequence of characters enclosed in quotes.

course = "Python for Beginners"

character = course[0]
print(character)

character = course[-1] # Negative indexing
print(character)

character = course[0:6] # Accessing more than one characters (lats character is excluded)
print(character)

character = course[0:] # This prints all characters assuming 0:length
print(character)

character = course[:3] # This prints from 0 to 3 assuming 0:...
print(character) 

character = course[:] # This prints all characters assuming 0:....
print(character)

character = course[-1:-5:-1] # For printing right to left using negative slicing
print(character)

character = course[-9:-1] # Accessing more than one characters using negative indexing
print(character)