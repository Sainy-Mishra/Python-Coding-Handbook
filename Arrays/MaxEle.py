n=int(input("Enter a number: "))
arr=[]

for i in range(n):
    arr.append(int(input("Enter the element: ")))

maximum=arr[0]
for num in arr:
    if num>maximum:
        maximum=num

print("Maximum is: ", maximum)