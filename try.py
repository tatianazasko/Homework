class Taxi:
    car = list["Car"]
    def __init__(self, count_passengers, is_baby, car):
        self.count_passengers = count_passengers
        count_passengers = int(input())
        self.is_baby = is_baby
        is_baby = int(input())
        if is_baby > 0: is_baby + 1
        self.car = car
@classmethod
def find_car (cls, car, count_passengers, is_baby):
    return cls( car, car - (count_passengers + is_baby))
@staticmethod
def car_ok (count_passengers, is_baby):
    return sum(count_passengers, is_baby) < car

taxi = Car(23,3,30)
