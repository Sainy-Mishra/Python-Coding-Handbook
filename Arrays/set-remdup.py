n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element: ")))

rev=list(set(arr))
print("Array without duplicates: ", rev)