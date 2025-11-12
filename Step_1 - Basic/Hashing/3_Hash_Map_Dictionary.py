n=int(input("Entered value : "))
ar1=[int(input(f"Enter element no. {i+1} : ")) for i in range(n)]

hash_map={}
for i in ar1:
    hash_map[i]=hash_map.get(i,0)+1

# for key, value in hash_map.items():
#     print(f"{key} -> {value}")

query=int(input("Enter no. of queries : "))
for _ in range(query):
    qno=int(input(f"Enter query no. {_+1} : "))
    print(hash_map.get(qno,0))
# Best-Avg Case -> Time complexity - O(1)
# Worst Case -> Time complexity - O(N) [happens once in a blue moon*]... Collision is when all your keys end up at the same hash index. This is when the worst case will happen.
# Hashing Methods -> 1. Division Method - > Linear Chaining - Done for Same % Value; 2. Folding Method; 3. Mid Square
max_freq = max(hash_map.values())
min_freq = min(hash_map.values())

max_freq_elements=[]
min_freq_elements=[]
for key, value in hash_map.items():
    if value == max_freq:
        max_freq_elements.append(key)
    if value == min_freq:
        min_freq_elements.append(key)

print(f"The Elements having the Maximum Frequency Value : {max_freq} are {max_freq_elements} ")
print(f"The Elements having the Minimum Frequency Value : {min_freq} are {min_freq_elements} ")