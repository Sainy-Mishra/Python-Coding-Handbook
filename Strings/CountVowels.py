s=input()
count=0

for i in s.lower():
    if i in "aeiou":
        count+=1

print("There are ", count, " vowels in ", s)