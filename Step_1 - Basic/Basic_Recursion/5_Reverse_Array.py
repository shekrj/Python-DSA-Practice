# def arr():
#     n=int(input("Size for array : "))
#     arr=[]
#     for i in range(n):
#         element=int(input(f"Enter element {i+1} : "))
#         arr.append(element)
#     return arr
# array=arr.reverse()
# print(array)
# print(array[::-1])

def revarr(arr, start, end):
    if start>=end:
        return
    arr[start], arr[end]= arr[end], arr[start]
    revarr(arr, start+1, end-1)
Arr=[1,2,3,4]
print(f"original array {Arr}")
revarr(Arr, 0, len(Arr)-1)
print(f"Reverse array {Arr}")
