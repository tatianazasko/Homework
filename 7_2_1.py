#2. Написать класс Taxi
#Конструктор класса принимает атрибуты:
#cars: list[Car] (список экземпляров класса Car)
#2.1 Реализовать метод find_car
#На вход метода поступают атрибуты: count_passengers,
# is_baby (количество пассажиров, наличие ребенка, примечание:
# количество пассажиров с учетом ребенка если он есть)
#На основании данных, вернуть объект Car из атрибута cars
# подходящий по параметрам и свободный (is_busy = False),
#у автомобиля сменить атрибут is_busy на значение True,
# если подходящего автомобиля нет, метод должен возвращать None

class Taxi:
    car = list[]
    def __init__(self, count_passengers, is_baby):
        self.count_passengers = count_passengers
        count_passengers = int(input())
        self.is_baby = is_baby
        is_baby = int(input())
        if is_baby > 0: is_baby + 1
        passengers = sum(is_baby, count_passengers)

    def __init__(self, cars):
        self.cars = cars
        cars = int(input("Number of seats:"))
        def __int__(self, car):
        self.car = car
        car = cars - passengers

#class Taxi:
  #  car = list["Car"]
   # def __init__(self, count_passengers, is_baby, car):
   #     self.count_passengers = count_passengers
   #     count_passengers = int(input())
    #    self.is_baby = is_baby
    #    is_baby = int(input())
     #   if is_baby > 0: is_baby + 1
     #   self.car = car
#@classmethod
#def find_car (cls, car, count_passengers, is_baby):
    #return cls( car, car - (count_passengers + is_baby))
#@staticmethod
#def car_ok (count_passengers, is_baby):
  #  return sum(count_passengers, is_baby) < car

#taxi = Car(23,3,30)
