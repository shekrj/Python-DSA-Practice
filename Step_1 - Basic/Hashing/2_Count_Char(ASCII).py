n=input("Entered String : ")

Hash_table=[0]*256
for i in n:
    Hash_table[ord(i)]+=1

query=int(input("Enter no. of queries : "))
for _ in range(query):
    qchar=input("Enter the character to query : ").strip()
    print(Hash_table[ord(qchar)])