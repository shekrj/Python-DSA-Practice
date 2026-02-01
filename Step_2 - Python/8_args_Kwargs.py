#ARGS
def func(*prices):
    print(sum(prices))

func(100, 200, 50)

#KWARGS
def create_user(**details):
    print(details)

create_user(name="Abhishek", age=22)
