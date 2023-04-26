#1. Написать класс Car
#Конструктор класса принимает атрибуты:
#color: str (цвет)
#count_passenger_seats: int (количество пассажирских мест)
#is_baby_seat: bool (наличие десткого кресла)
#is_busy: bool (определяется внутри конструктора со значением False, не принимается на вход)
#1.1 Написать магический метод __str__ выводящий форматированную строку с информацией об автомобиле

class Car:
    car_description = 'Car'
    def __init__(self, color, count_passenger_seats, is_baby_seat, is_busy):
        self.color = color
        color = str(input())
        self.count_passenger_seats = count_passenger_seats
        count_passenger_seats = int(input())
        self.is_baby_seat = is_baby_seat
        is_baby_seat = int(input())
        if is_baby_seat > 0: is_baby_seat + 1
        self.is_busy = is_busy
        is_busy = int(input())
        if is_busy > 0: is_busy + 1

        def dict(self) -> dict:
            return{'color': self.color,
                'passengers': self.count_passenger_seats,
                'kids': self.is_baby_seat,
                'busy seats': self.is_busy
            }

            def __str__(self):
                return f'Car: color={self.color}, passengers={self.count_passenger_seats}  kids={self.is_baby_seat} busy seats = {self.is_busy}'


print(Car)