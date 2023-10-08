def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)

print(is_isogram("India"))  
print(is_isogram("read"))  
print(is_isogram("DOOg")) 
print(is_isogram("   "))