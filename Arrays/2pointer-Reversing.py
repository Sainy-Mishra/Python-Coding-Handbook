n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element: ")))

left=0
right=n-1
while left<right:
    arr[left], arr[right]=arr[right], arr[left]
    left+=1
    right-=1

print("Reversed Array: ", arr)