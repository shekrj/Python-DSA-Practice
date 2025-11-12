# def main():
#     # Input the size of the array
#     n = int(input("Enter the size of the array: "))
#     arr = list(map(int, input("Enter the elements of the array: ").split()))
#     # Precompute:
#     hash_table = [0] * 13
#     for num in arr:
#         hash_table[num] += 1
#     # Queries:
#     q = int(input("Enter the number of queries: "))
#     for _ in range(q):
#         number = int(input("Enter the number to query: "))
#         # Fetching:
#         print(hash_table[number])
# if __name__ == "__main__":
#     main()
n=int(input("Entered Size for Array : "))
arr1=[]
for i in range(n):
    element=int(input(f"Element no. {i+1} : "))
    arr1.append(element)
print(arr1)

hash_table=[0]*13
for elements in arr1:
    hash_table[elements]+=1

query=int(input("No. of queries : "))
for _ in range(query):
    qnum=int(input("Entered no. for query : "))
    if qnum>=0 and qnum<13:
        print(hash_table[qnum])
    else:
        print("Query number OUT OF RANGE!!")

# n=int(input("Enter size for an Array : "))
# arr1=[int(input(f"Enter Element {i+1}")) for i in range(n)]   ## MORE PYTHONIC WAY FOR CREATING A LIST