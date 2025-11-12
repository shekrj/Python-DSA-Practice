def main():
    # Input the size of the array
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))

    # Precompute using a dictionary for hashing
    hash_table = {}
    for num in arr:
        hash_table[num] = hash_table.get(num, 0) + 1

    # Queries:
    q = int(input("Enter the number of queries: "))
    for _ in range(q):
        number = int(input("Enter the number to query: "))
        # Fetching and handling cases where the number is not in the array
        print(hash_table.get(number, 0))

if __name__ == "__main__":
    main()