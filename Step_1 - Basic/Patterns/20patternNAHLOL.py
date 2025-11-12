def pattern(n: int):
    # Initializing the spaces
    spaces = 2 * n - 2

    # Outer loop for printing rows
    for i in range(1, 2 * n):
        # Calculate the number of stars for each half
        stars = i if i <= n else 2 * n - i

        # Print the stars for the current row (first half)
        for _ in range(stars):
            print("*", end="")

        # Print the spaces
        for _ in range(spaces):
            print(" ", end="")

        # Print the stars for the current row (second half)
        for _ in range(stars):
            print("*", end="")

        # Move to the next row
        print()

        # Adjust the number of spaces for the next row
        if i < n:
            spaces -= 2
        else:
            spaces += 2


# Example usage
n = int(input("Enter the value for n: "))
pattern(n)
