def total(**kwargs): #keyword arguments variable length
    return sum(kwargs.values()) #stored as a dictionary

print(total(a=1,b=2,c=3,d=4,e=5))