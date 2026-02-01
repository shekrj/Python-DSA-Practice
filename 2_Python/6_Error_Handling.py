try:
    a=10
    b=0
    res=a/b
    print(res)
except Exception as e:
    print(f'Error: {e}')
finally:
    print("Program ended.")

