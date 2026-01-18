import string
alphabets={}
for i in string.ascii_lowercase:
    alphabets[i]=0

print( alphabets )   
sentence= input("Enter a sentence").lower()

for i in sentence:
    if i in alphabets:
        alphabets[i]+=1
print (alphabets)

panagram=False
for i in alphabets:
    if alphabets[i]==0:
        print("Its not a panagram")
        break

    else:
        panagram=True
if panagram:
    print("Its a panagram")