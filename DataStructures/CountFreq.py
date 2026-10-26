l=[1,2,3,2,1,2,3,4]
freq={}

for n in l:
    freq[n]=freq.get(n,0)+ 1 #dict.get(element, default)

print(freq)