from threading import Thread
from time import sleep


class Knight(Thread):  # класс Knight, содержащий два метода (__init__, run), наследуемый от материнского класса Thread
    def __init__(self, name, power):
        super().__init__()  # наследование __init__ от родительского класса Thread
        self.name = name  # атрибут name - имя рыцаря
        self.power = power  # aтрибут power - сила рыцаря

    def run(self):
        enemies = 100  # Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100)
        number_of_days = 0
        print(
            f"{self.name}, на нас напали!")  # При запуске потока должна выводится надпись
        while enemies > 0:  # цикл работает пока количество врагов больше 0
            enemies -= self.power  # В процессе сражения количество врагов уменьшается на power текущего рыцаря
            sleep(1)
            number_of_days += 1  # счетчик дней, который увеличивается на один
            print(f"{self.name} сражается {number_of_days} день(дня).., осталось {enemies} воинов.")  # ежедневный вывод
        print(f"{self.name} одержал победу спустя {number_of_days} дней(дня)!")  # итоговый вывод


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
