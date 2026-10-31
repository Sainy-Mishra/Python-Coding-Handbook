n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element: ")))

unique = sorted(set(arr))

if len(unique) >= 2:
    print("Second Largest Number: ",unique[-2])
else:
    print("No second largest")