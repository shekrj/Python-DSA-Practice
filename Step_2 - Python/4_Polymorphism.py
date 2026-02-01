# Example 1: Method overriding (OOP polymorphism)
class Animal:
    def sound(self):
        print("Noise")

class Dog(Animal):
    def sound(self, yo):
        print("Barking")

class Cat(Animal):
    def sound(self):
        print("Meow")

def main():
    a1=Animal()
    a1.sound()
    yo='yo'
    d1=Dog()
    d1.sound(yo)

    c1=Cat()
    c1.sound()

if __name__=='__main__':
    main()

# Example 2: Operator overloading (another type of polymorphism)
print(5 + 10)     # 15 (integers)
print("Hi " + "Abhi")  # Hi Abhi (strings)
