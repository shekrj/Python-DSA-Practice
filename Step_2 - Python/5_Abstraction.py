from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Barking")

def main():
    d = Dog()
    d.sound()

if __name__ == "__main__":
    main()
