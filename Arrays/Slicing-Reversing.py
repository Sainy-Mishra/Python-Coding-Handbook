n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element: ")))

arr=arr[::-1]
print("Reversed array: ", arr)