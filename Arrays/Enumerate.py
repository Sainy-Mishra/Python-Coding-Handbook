n=int(input("Enter a number: "))
arr=[]

for i in range(n):
    arr.append(int(input("Enter the element: ")))

for index, value in enumerate(arr):
    print(index, value)