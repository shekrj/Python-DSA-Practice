try:
    with open('File.txt', 'r') as f:
        data=f.read()
        print(data)
except Exception as e:
    print(f'Error: {e}')
finally:
    print("File operation completed")

