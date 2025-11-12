def secLargest(arr):
    n=len(arr)
    if n<2:
        return
    
    largest=float('-inf')
    secondlargest=float('-inf')

    for i in range(n):
        if arr[i]>largest:
            secondlargest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>secondlargest:
            secondlargest=arr[i]
    
    if secondlargest==float('-inf'):
        return "All elements are same !!"
    return largest, secondlargest

def secSmallest(arr):
    n=len(arr)
    if n<2:
        return "Array must have at least two elements"
    
    smallest=float('inf')
    secondsmallest=float('inf')

    for i in range(n):
        if arr[i]<smallest:
            secondsmallest=smallest
            smallest=arr[i]
        elif arr[i]>smallest and arr[i] < secondsmallest:
            secondsmallest=arr[i]
        
    if secondsmallest==float('inf'):
            return "All elements are same"
    return smallest, secondsmallest




n=int(input("Enter size for an array : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(secLargest(arr1))
print(secSmallest(arr1))