#List comprehension
temp=[1,2,3,4,5]
square_even=[x*x for x in temp if x%2==0]
print(square_even)

#Generator Expression
gen_example=(x*x for x in temp)
res=sum(gen_example)
print(res)

#Encapsulation
class ATM:
    def __init__(self, balance):
        self.__balance=balance
    
    def get_balance(self):
        return self.__balance

def main():
    temp=100
    ob1=ATM(temp)
    print(ob1.get_balance())
    try:
        print(ob1.__balance)
    except Exception as e:
        print(f'Error: {e}')
    finally:
        print('Encapsulation Example because the variable is Private')

if __name__=="__main__":
    main()

# Polymorphism
# Runtime poly
class Animal:
    def sound(self):
        print('Some generic sound')

class Dog(Animal):
    def sound(self):
        print('Bark')

def main():
    a1=Animal()
    d1=Dog()

    a1.sound()
    d1.sound()
main()

#Compile time
print(5+10)
print("5"+"10")

# Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

def main():
    try:
        a1=Animal()
        a1.sound()
    except Exception as e:
        print(f'Error: {e}')
    finally:
        print('Ran abstract for practice')
    d1=Dog()
    d1.sound()

if __name__=='__main__':
    main()

# Error Handling
a=10
b=0
try:
    print(a/b)
except Exception as e:
    print(f'Error: {e}')
finally:
    print("Operation completed")

# File Handling
try:
    with open('file.txt', 'r') as f:
        data=f.read()
except Exception as e:
    print(f'Error: {e}')
finally:
    print("File operation done")


# *ARGS AND **KWARGS
def func1(*numbers):
    print((sum(numbers)))

func1(1,2,3,4)

def func2(**detail):
    print(detail)

func2(name='Abhishek', system_id=101)