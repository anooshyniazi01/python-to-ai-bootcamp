message = "hello my name is anosh"
print(message[0])
print(message[5])
print(message[-1])
# Slicing
print(message[0:5])
print(message[6:14])
print(message[:5])
print(message[6:])
# Original string
print(message)
# String methods
print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())
# Removing spaces
st = "   Python Programming   "
print(st.strip())
print(st.lstrip())
print(st.rstrip())
# Replacing words
print(message.replace("hello", "Hey"))
# Splitting a string
s = "apple,banana,mango,orange"
print(s.split(","))
# Finding length
print(len(message))
# Counting characters
print(message.count("a"))
# Finding a word
print(message.find("name"))
# Checking the beginning and ending
print(message.startswith("hello"))
print(message.endswith("anosh"))
