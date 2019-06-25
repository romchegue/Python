# File: composition.py

class Lunch:
    def __init__(self): # Создает и встраивает Customer и Employee
        self.client = Customer()
        self.server = Employee()
    def order(self, foodName): # Имитирует прием заказа
        self.client.placeOrder(foodName, self.server)     		
    def result(self): # Запрашивает у клиента название блюда
        self.client.printFood()

class Customer:
    def __init__(self): # Инициализирует название блюда значением None
        self.food = None
    def placeOrder(self, foodName, employee): # Передает заказ официанту
        self.food = employee.takeOrder(foodName)    
    def printFood(self): # Выводит название блюда
        print(self.food.name)
        
class Employee:
    def takeOrder(self, foodName): # Возвращает блюдо с указанным названием
        return Food(foodName) 
		
class Food:
    def __init__(self, name=''):	# Сохраняет название блюда
        self.name = name


if __name__ == '__main__':
    scenerio = Lunch()
    scenerio.order(input('Enter the name of the dish:\n'))
    scenerio.result()

