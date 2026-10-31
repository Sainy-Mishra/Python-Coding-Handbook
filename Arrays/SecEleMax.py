n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element: ")))

largest=second=None

for num in arr:
    if largest is None or num > largest:
        second = largest
        largest = num

    elif num != largest and (second is None or num > second):
        second = num

if second==None:
    print("Largest number: ",largest)
    print("No second largest.")
else:
    print("Largest number: ", largest)
    print("Second largest number: ",second)