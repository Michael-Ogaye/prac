string = "Hello, how are you doing today? I hope you are doing well."
substring = "doing"

# Using a loop and string slicing
indices = []
for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        indices.append(i)

print("Substring", substring, "found at indices:", indices)

# Using the `find()` method in a loop
indices = []
index = -1
while True:
    index = string.find(substring, index + 1)
    if index == -1:
        break
    indices.append(index)

print("Substring", substring, "found at indices:", indices)

# Using the `findall()` method of the `re` module
import re
indices = [match.start() for match in re.finditer(substring, string)]
print("Substring", substring, "found at indices:", indices)

