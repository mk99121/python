# Open the file in read mode ('r')
with open('example.txt', 'r') as file:
    first_line = file.readline()

print("File Content:")
print(first_line)


# Open the file in read mode ('r')
with open('example.txt', 'r') as file:
    # Read the first line and discard it
    file.readline()
    
    # Read the second line
    second_line = file.readline()

print("Second Line:")
print(second_line)
