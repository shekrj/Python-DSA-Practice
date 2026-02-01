#Encapsulation
class Balance:
    def __init__(self, balance):
        self.__bal=balance
    
    def get_Balance(self):
        return self.__bal

def main():
    ob1=Balance(100)
    print(ob1.get_Balance())
main()
