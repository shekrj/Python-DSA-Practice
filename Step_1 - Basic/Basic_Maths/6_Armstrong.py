n=int(input("Entered value : "))
count=len(str(abs(n)))
sum=0
for i in str(n):
    digits=int(i)
    sum+=digits**count
if sum==n:
    print("true")
else:
    print("false")

# def checkArmstrong(n):
#     count = len(str(abs(n)))  # Get the number of digits
#     sum = 0  # Initialize sum to 0
#     for i in str(abs(n)):  # Iterate through each digit of the number
#         digits = int(i)
#         sum += digits ** count  # Add the digit raised to the power of count
#     return "true" if sum == n else "false"  # Return "true" or "false"

# # Example usage:
# n = int(input("Enter a number: "))
# print(checkArmstrong(n))  # Expected to print true or false

