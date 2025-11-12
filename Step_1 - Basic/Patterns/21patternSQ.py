def hollow_square(n: int):
    # Outer loop for number of rows
    for i in range(n):
        # Inner loop for printing the stars at borders only
        for j in range(n):
            # Check if the current position is a border
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print("*", end="")
            else:
                # If not a border index, print a space
                print(" ", end="")
        # Move to the next line after each row
        print()


# Example usage
n = int(input("Enter the size of the square: "))
hollow_square(n)
