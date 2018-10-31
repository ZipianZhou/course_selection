class Course:
    def __init__(self, name, period, price):
        if not isinstance(period, int):
            raise TypeError("Course period must be an int")

        if not isinstance(price, int):
            raise TypeError("Course price must be an int")

        if not isinstance(name, str):
            raise TypeError("Course name must be a str")

        self.__name = name
        self.__period = period
        self.__price = price

    def getName(self):
        return self.__name

    def getPeriod(self):
        return self.__period

    def setPeriod(self, period):
        if not isinstance(period, int):
            raise TypeError("Course period must be an int")  
        self.__period = period

    def getPrice(self):
        return self.__price

    def setPeriod(self, price):
        if not isinstance(price, int):
            raise TypeError("Course price must be an int")   
        self.__price = price

