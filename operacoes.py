# A class who has the operations

# Just a little curiosity, I could use the "Assert" method, within the functions, but I didn't think it was necessary to check, but to exemplify:
# assert isinstance(value,int),"Is not a Integer..."


class Operacoes():
    def __init__(self):
        return
        
    def sum(self,i:int , j:int) -> int:
        self.__i = i
        self.__j = j
        return self.__i + self.__j

    def subtraction(self,i:int , j:int ) -> int:
        self.__i = i
        self.__j = j
        return self.__i - self.__j

    def multiply(self,i:int, j:int) -> int:
        self.__i = i
        self.__j = j
        return self.__i * self.__j

    def divide(self,i:int, j:int) -> int or float:
        self.__i = i
        self.__j = j
        return self.__i / self.__j

    def divideRest(self,i:int, j:int) -> int or float:
        self.__i = i
        self.__j = j
        return self.__i % self.__j
