import string
vowels={"a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0}

consonants={}
for i in string.ascii_lowercase:
    if i not in vowels:
        consonants[i]=0
print (consonants)
