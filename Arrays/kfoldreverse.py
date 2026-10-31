n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element: ")))

k=int(input("Enter the value of fold: "))

k = k % len(arr)

arr1 = arr[k:] + arr[:k]

print("Left k fold: ", arr1)

arr2=arr[-k:]+arr[:-k]

print("Right k fold: ", arr2)