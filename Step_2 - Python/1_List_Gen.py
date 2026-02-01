# List Comprehension and Generator Expression Example -> 
from typing import List
class Solution:
    def func(self, temp: List[int]) -> None:
        list_CompEx=[x*x for x in temp]
        print(list_CompEx)
        
        genExp=(x*x for x in temp)
        print(sum(genExp))


def main():
    ob1=Solution()
    arr=[]
    size=int(input("Enter Size for Arr: "))
    for i in range(size):
        element=int(input(f"Enter element {i+1} : "))
        arr.append(element)
    ob1.func(arr)
main()
