n = int(input("Enter value for n: "))

# Outer loop for the number of rows
for i in range(n):
    # Using a full if-else block to determine the starting value for each row
    if i % 2 == 0:  # If row index is even
        start = 1
    else:  # If row index is odd
        start = 0
    
    # Inner loop to print alternating 1's and 0's
    for j in range(i + 1):  # Print i + 1 numbers in each row
        print(start, end="")  # Print the current value of start without newline
        start = 1 - start  # Alternate between 1 and 0
    
    # Move to the next line after each row
    print()
