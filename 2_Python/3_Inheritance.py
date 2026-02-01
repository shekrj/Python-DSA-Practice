#Inheritance
class Animal:
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meow")

def main():
    d1=Dog()
    d1.eat()
    d1.bark()
    d1.sleep()
    print()
    c1=Cat()
    c1.eat()
    c1.meow()
    c1.sleep()
if __name__=='__main__':
    main()

''' 
    - Every Python file has a special built-in variable called __name__
    - If you run the file directly, Python sets __name__ = "__main__" 
    
'''